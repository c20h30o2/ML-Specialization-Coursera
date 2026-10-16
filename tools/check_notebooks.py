"""Execute notebooks with this Python environment, without overwriting originals."""
import argparse
import concurrent.futures
import json
import os
from pathlib import Path
import sys
import tempfile
import time

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpec


class CurrentPythonKernel(KernelManager):
    @property
    def kernel_spec(self):
        return KernelSpec(
            argv=[sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            display_name="current Python", language="python",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=600, help="Seconds per cell")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    paths = args.paths or sorted(
        p for p in root.rglob("*.ipynb")
        if not any(part.startswith(".") for part in p.relative_to(root).parts)
    )
    output = (args.output or Path(tempfile.mkdtemp(prefix="ml-notebooks-"))).resolve()
    output.mkdir(parents=True, exist_ok=True)
    paths = [p.resolve() for p in paths if output not in p.resolve().parents]
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "TF_NUM_INTRAOP_THREADS", "TF_NUM_INTEROP_THREADS"):
        os.environ.setdefault(key, "2")

    def execute(item):
        index, path = item
        started = time.monotonic()
        result = {"path": str(path), "status": "passed"}
        notebook = None
        try:
            notebook = nbformat.read(path, as_version=4)
            # Clear saved outputs so an early failure cannot report stale errors.
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    cell.outputs = []
                    cell.execution_count = None
            NotebookClient(
                notebook, timeout=args.timeout,
                kernel_manager_class=CurrentPythonKernel,
                resources={"metadata": {"path": str(path.parent)}},
            ).execute()
        except Exception as exc:
            result.update(status="failed", error=str(exc))
        if notebook is not None:
            result["errors"] = [
                {"cell": i + 1, "type": out.ename, "message": out.evalue}
                for i, cell in enumerate(notebook.cells)
                for out in cell.get("outputs", []) if out.output_type == "error"
            ]
            nbformat.write(notebook, output / f"{index:03d}.ipynb")
        result["seconds"] = round(time.monotonic() - started, 1)
        (output / f"{index:03d}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print(f"{result['status']}: {path.name}", flush=True)
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(execute, enumerate(paths)))
    (output / "summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2))
    passed = sum(r["status"] == "passed" for r in results)
    print(f"{passed}/{len(results)} passed; reports: {output}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
