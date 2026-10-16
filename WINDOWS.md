# Windows + VS Code 运行说明

适用于 Windows 10/11 x64、Conda 和 VS Code 的 Jupyter 插件，使用 CPU 运行 TensorFlow。

## 安装环境

1. 安装 Miniconda 或 Anaconda，以及 VS Code。安装 VS Code 的 **Python**（Microsoft）和 **Jupyter**（Microsoft）扩展。
2. 下载仓库 ZIP 后完整解压，或用 Git 克隆。不要只复制 `.ipynb`，实验还需要同目录的 Python 模块、数据和图片。
3. 打开 **Anaconda Prompt / Miniconda Prompt**，进入仓库根目录，执行：

```bat
conda env create -f environment-windows.yml
conda activate ml
python -m ipykernel install --user --name ml --display-name "Python (ml)"
python -m pip check
dot -V
```

如果电脑已有名为 `ml` 的环境，先在 YAML 中把 `name` 改为 `ml-course`，并同步替换后续命令中的环境名和内核名，避免混用已有环境。

环境文件通过 conda-forge 安装 Windows 编译好的 Box2D 和 Graphviz，其余依赖使用 `requirements-ml.txt`；无需手动编译 Box2D，也无需安装 JupyterLab。

## 在 VS Code 中运行

1. 用 VS Code 的 **打开文件夹**打开仓库根目录。
2. 打开任意 notebook，右上角点击 **选择内核**，选择 `Python (ml)` 或对应的 `ml` Python 环境。
3. 从第一个单元格开始执行。仓库设置让工作目录跟随 notebook 所在目录。
4. 如果依赖安装后 VS Code 已经开着，重新选择内核并重启内核。可在临时单元格执行 `import sys; print(sys.executable)`，确认路径位于 Conda 的 `envs\ml`。

`%matplotlib widget` 的交互图通过 `ipympl` 显示。请保留仓库的 `.vscode/settings.json`；归档 notebook 会自动定位其父目录资源。

## 检查与限制

可在已激活环境的终端中批量执行：

```bat
python tools/check_notebooks.py
```

结果保存到独立临时目录，不覆盖源 notebook；存在未填写练习时，脚本退出码为 1。

Linux `ml` 环境下已检查 67 个 notebook：42 个完整通过、4 个为空白或占位、21 个在未完成练习处停止。练习答案保持留空，停止点之后的单元格尚未验证。详情见 [检查报告](notebook-check-report.md)。

Windows 配置已核对 Python 3.11 / win-64 安装包可用性；尚未在真实 Windows 主机执行 notebook，Linux 的通过结果不能代替 Windows 实机验证。
