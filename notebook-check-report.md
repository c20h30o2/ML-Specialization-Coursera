# Notebook 执行检查报告

检查日期：2026-10-16。环境：`ml`，Python 3.11。

递归检查当前目录下 67 个 notebook，包含 `archive`、`betaversion` 和 `pre_414`；不包括隐藏的自动检查点。

结果：42 个包含实际代码的 notebook 从头到尾执行通过；4 个空白或占位文件；21 个因练习尚未填写而停止。所有 `START CODE HERE` / `END CODE HERE` 之间的内容均保持原样。

## 已修复

- 补齐 TensorFlow CPU、XGBoost、Gym、Box2D、pydot、tabulate、imageio 和 notebook 执行工具等依赖；`pip check` 通过。
- 修正归档 notebook 和两份错放副本的辅助模块、样式及数据目录定位。
- 修正旧版实验缺失的 pyplot 导入、`w1` 变量笔误，以及被标为代码的说明文本。
- 将 XGBoost 的 `early_stopping_rounds` 移到模型构造函数；移除 notebook 中每次执行都会安装包的命令。
- 使用内置 `pickle` 替代 `pickle5`，使用 `bool` 替代已移除的 `np.bool`。
- 强化学习实验在无 DISPLAY 时使用 SDL dummy 驱动，已验证环境创建、图像渲染和动作执行。
- 修正 beta ReLU 实验中模型创建与预测的顺序、TensorFlow Activation API，以及聚类的 `affinity` → `metric` 参数。

## 验证范围

每个 notebook 使用独立的 ml Python 内核，从其所在目录顺序执行，最终每个单元格超时上限为 600 秒。后续发现的问题修复后进行了针对性复验。原 notebook 的已保存输出未被批量刷新；详细执行副本和 JSON 结果位于 `/tmp/ml-notebook-audit/`，最终汇总为 `final-summary.json`。

练习失败处之后的单元格尚未验证，包含后续训练和强化学习完整训练。未进行浏览器内按钮、拖动等人工交互验证；这里只验证了单元格执行和控件创建。空白文件不计入实际代码通过数。

## 复现

依赖版本记录在 `requirements-ml.txt`。Graphviz 的系统命令 `dot` 已存在；Box2D 源码安装方式见依赖文件开头。

```bash
conda run -n ml python tools/check_notebooks.py
# 也可在末尾传入一个或多个 notebook 路径，只检查指定文件。
```

脚本使用启动它的 Python 解释器作为 notebook 内核，将结果写入独立临时目录，不覆盖源 notebook。存在练习空白时退出码为 1，这是保留空白后的预期结果。可使用 `--output` 指定结果目录、`--timeout` 设置每单元格秒数。

## 逐文件结果

| Notebook | 结果 | 停止位置（从 1 开始的单元格序号） |
| --- | --- | --- |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 1/labs/C1_W1_Lab01_Python_Jupyter_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%201/labs/C1_W1_Lab01_Python_Jupyter_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 1/labs/C1_W1_Lab02_Model_Representation_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%201/labs/C1_W1_Lab02_Model_Representation_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 1/labs/C1_W1_Lab03_Cost_function_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%201/labs/C1_W1_Lab03_Cost_function_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 1/labs/C1_W1_Lab04_Gradient_Descent_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%201/labs/C1_W1_Lab04_Gradient_Descent_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 1/labs/Untitled.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%201/labs/Untitled.ipynb) | 空白 / 占位 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/Week 2 Programming Assignment/C1_W2_Linear_Regression.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/Week%202%20Programming%20Assignment/C1_W2_Linear_Regression.ipynb) | 练习未完成 | 单元格 24：AssertionError — Case 2: Cost must be 2 but got 0 |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W2_Lab01_Python_Numpy_Vectorization_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W2_Lab01_Python_Numpy_Vectorization_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W2_Lab02_Multiple_Variable_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W2_Lab02_Multiple_Variable_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W2_Lab03_Feature_Scaling_and_Learning_Rate_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W2_Lab03_Feature_Scaling_and_Learning_Rate_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W2_Lab04_FeatEng_PolyReg_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W2_Lab04_FeatEng_PolyReg_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W2_Lab05_Sklearn_GD_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W2_Lab05_Sklearn_GD_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W2_Lab06_Sklearn_Normal_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W2_Lab06_Sklearn_Normal_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/C1_W3_Lab01_Classification_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/C1_W3_Lab01_Classification_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 2/labs/archive/C1_W2_Lab01_Python_Numpy_Vectorization_Soln-Copy1.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%202/labs/archive/C1_W2_Lab01_Python_Numpy_Vectorization_Soln-Copy1.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/Week 3 Programming Assignment/C1_W3_Logistic_Regression.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/Week%203%20Programming%20Assignment/C1_W3_Logistic_Regression.ipynb) | 练习未完成 | 单元格 20：NameError — name 'g' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/Week 3 Programming Assignment/archive/20230213_C1_W3_Logistic_Regression.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/Week%203%20Programming%20Assignment/archive/20230213_C1_W3_Logistic_Regression.ipynb) | 练习未完成 | 单元格 20：NameError — name 'g' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/Week 3 Programming Assignment/archive/C1_W3_Logistic_Regression-Copy1.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/Week%203%20Programming%20Assignment/archive/C1_W3_Logistic_Regression-Copy1.ipynb) | 练习未完成 | 单元格 19：NameError — name 'g' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/Week 3 Programming Assignment/archive/C1_W3_Logistic_Regression-Copy2.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/Week%203%20Programming%20Assignment/archive/C1_W3_Logistic_Regression-Copy2.ipynb) | 练习未完成 | 单元格 19：NameError — name 'g' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab01_Classification_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab01_Classification_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab02_Sigmoid_function_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab02_Sigmoid_function_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab03_Decision_Boundary_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab03_Decision_Boundary_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab04_LogisticLoss_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab04_LogisticLoss_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab05_Cost_Function_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab05_Cost_Function_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab06_Gradient_Descent_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab06_Gradient_Descent_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab07_Scikit_Learn_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab07_Scikit_Learn_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab08_Overfitting_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab08_Overfitting_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Lab09_Regularization_Soln.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Lab09_Regularization_Soln.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/C1_W3_Logistic_Regression.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/C1_W3_Logistic_Regression.ipynb) | 练习未完成 | 单元格 20：NameError — name 'g' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/archive/C1_W3_Lab05_Cost_Function_Soln-Copy1.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/archive/C1_W3_Lab05_Cost_Function_Soln-Copy1.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/archive/C1_W3_Lab05_Cost_Function_Soln-Copy2.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/archive/C1_W3_Lab05_Cost_Function_Soln-Copy2.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/archive/C1_W3_Lab09_Regularization_Soln-Copy1.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/archive/C1_W3_Lab09_Regularization_Soln-Copy1.ipynb) | 通过 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab01_Sigmoid_function.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab01_Sigmoid_function.ipynb) | 练习未完成 | 单元格 6：SyntaxError — invalid syntax (1371897842.py, line 4) |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab02_Decision_Boundary.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab02_Decision_Boundary.ipynb) | 练习未完成 | 单元格 9：SyntaxError — invalid syntax (1687675596.py, line 5) |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab03_Cost_Function.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab03_Cost_Function.ipynb) | 练习未完成 | 单元格 12：NameError — name 'cost' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab04_Gradient_Descent.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab04_Gradient_Descent.ipynb) | 练习未完成 | 单元格 12：NameError — name 'gradient' is not defined |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab05_One_Vs_All.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab05_One_Vs_All.ipynb) | 空白 / 占位 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab06_Regularized_Cost.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab06_Regularized_Cost.ipynb) | 空白 / 占位 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab07_Regularized_Gradient_Descent.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab07_Regularized_Gradient_Descent.ipynb) | 空白 / 占位 | — |
| [Course 1 - Supervised Machine Learning (Regression and Classification)/Week 3/labs/pre_414/C1_W3_Lab08_Scikit_Learn.ipynb](Course%201%20-%20Supervised%20Machine%20Learning%20%28Regression%20and%20Classification%29/Week%203/labs/pre_414/C1_W3_Lab08_Scikit_Learn.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 1/Week 1 Programming Assignment/C2_W1_Assignment.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/Week%201%20Programming%20Assignment/C2_W1_Assignment.ipynb) | 练习未完成 | 单元格 24：AssertionError — Wrong number of layers. Expected 3 but got 0 |
| [Course 2 - Advanced Learning Algorithms/Week 1/Week 1 Programming Assignment/archive/20230130_C2_W1_Assignment.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/Week%201%20Programming%20Assignment/archive/20230130_C2_W1_Assignment.ipynb) | 练习未完成 | 单元格 24：AssertionError — Wrong number of layers. Expected 3 but got 0 |
| [Course 2 - Advanced Learning Algorithms/Week 1/Week 1 Programming Assignment/archive/C2_W1_Assignment-Copy1.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/Week%201%20Programming%20Assignment/archive/C2_W1_Assignment-Copy1.ipynb) | 练习未完成 | 单元格 23：AssertionError — Wrong number of layers. Expected 3 but got 0 |
| [Course 2 - Advanced Learning Algorithms/Week 1/labs/C2_W1_Lab01_Neurons_and_Layers.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/labs/C2_W1_Lab01_Neurons_and_Layers.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 1/labs/C2_W1_Lab02_CoffeeRoasting_TF.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/labs/C2_W1_Lab02_CoffeeRoasting_TF.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 1/labs/C2_W1_Lab03_CoffeeRoasting_Numpy.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/labs/C2_W1_Lab03_CoffeeRoasting_Numpy.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 1/labs/archive/20230202_C2_W1_Lab02_CoffeeRoasting_TF.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%201/labs/archive/20230202_C2_W1_Lab02_CoffeeRoasting_TF.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/Week 2 Programming Assignment/C2_W2_Assignment.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/Week%202%20Programming%20Assignment/C2_W2_Assignment.ipynb) | 练习未完成 | 单元格 12：NameError — name 'a' is not defined |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/C2_W2_Multiclass_TF.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/C2_W2_Multiclass_TF.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/C2_W2_Relu.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/C2_W2_Relu.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/C2_W2_SoftMax.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/C2_W2_SoftMax.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/archive/C2_W2_SoftMax-Copy1.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/archive/C2_W2_SoftMax-Copy1.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/archive/C2_W2_SoftMax-Copy2.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/archive/C2_W2_SoftMax-Copy2.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/betaversion/C2_W2_Multiclass_TF.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/betaversion/C2_W2_Multiclass_TF.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/betaversion/C2_W2_Relu.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/betaversion/C2_W2_Relu.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/betaversion/C2_W2_SoftMax-Copy1.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/betaversion/C2_W2_SoftMax-Copy1.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 2/labs/betaversion/C2_W2_SoftMax.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%202/labs/betaversion/C2_W2_SoftMax.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 3/Week 3 Programming Assignment/C2_W3_Assignment.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%203/Week%203%20Programming%20Assignment/C2_W3_Assignment.ipynb) | 练习未完成 | 单元格 12：IndentationError — expected an indented block after 'for' statement on line 14 (807786573.py, line 21) |
| [Course 2 - Advanced Learning Algorithms/Week 3/labs/C2W3_Lab_01_Model_Evaluation_and_Selection.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%203/labs/C2W3_Lab_01_Model_Evaluation_and_Selection.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 3/labs/C2W3_Lab_02_Diagnosing_Bias_and_Variance.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%203/labs/C2W3_Lab_02_Diagnosing_Bias_and_Variance.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 4/Week 4 Programming Assignment/C2_W4_Decision_Tree_with_Markdown.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%204/Week%204%20Programming%20Assignment/C2_W4_Decision_Tree_with_Markdown.ipynb) | 练习未完成 | 单元格 18：AssertionError — Entropy must be 1 with same ammount of ones and zeros |
| [Course 2 - Advanced Learning Algorithms/Week 4/labs/C2_W4_Lab_01_Decision_Trees.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%204/labs/C2_W4_Lab_01_Decision_Trees.ipynb) | 通过 | — |
| [Course 2 - Advanced Learning Algorithms/Week 4/labs/C2_W4_Lab_02_Tree_Ensemble.ipynb](Course%202%20-%20Advanced%20Learning%20Algorithms/Week%204/labs/C2_W4_Lab_02_Tree_Ensemble.ipynb) | 通过 | — |
| [Course 3 - Unsupervised Learning, Recommenders, Reinforcement Learning/Week 1/Week 1 Programming Assignment/Anomaly Detection Programming Assignment/C3_W1_Anomaly_Detection.ipynb](Course%203%20-%20Unsupervised%20Learning%2C%20Recommenders%2C%20Reinforcement%20Learning/Week%201/Week%201%20Programming%20Assignment/Anomaly%20Detection%20Programming%20Assignment/C3_W1_Anomaly_Detection.ipynb) | 练习未完成 | 单元格 20：NameError — name 'mu' is not defined |
| [Course 3 - Unsupervised Learning, Recommenders, Reinforcement Learning/Week 1/Week 1 Programming Assignment/k-means/C3_W1_KMeans_Assignment.ipynb](Course%203%20-%20Unsupervised%20Learning%2C%20Recommenders%2C%20Reinforcement%20Learning/Week%201/Week%201%20Programming%20Assignment/k-means/C3_W1_KMeans_Assignment.ipynb) | 练习未完成 | 单元格 13：AssertionError — Wrong values |
| [Course 3 - Unsupervised Learning, Recommenders, Reinforcement Learning/Week 2/Week 2 Programming Assignment/Collaborative Filtering/C3_W2_Collaborative_RecSys_Assignment.ipynb](Course%203%20-%20Unsupervised%20Learning%2C%20Recommenders%2C%20Reinforcement%20Learning/Week%202/Week%202%20Programming%20Assignment/Collaborative%20Filtering/C3_W2_Collaborative_RecSys_Assignment.ipynb) | 练习未完成 | 单元格 25：AssertionError — Wrong value. Expected 27, got 0. Check the regularization term |
| [Course 3 - Unsupervised Learning, Recommenders, Reinforcement Learning/Week 2/Week 2 Programming Assignment/Deep Learning Recommender Systems/C3_W2_RecSysNN_Assignment.ipynb](Course%203%20-%20Unsupervised%20Learning%2C%20Recommenders%2C%20Reinforcement%20Learning/Week%202/Week%202%20Programming%20Assignment/Deep%20Learning%20Recommender%20Systems/C3_W2_RecSysNN_Assignment.ipynb) | 练习未完成 | 单元格 26：ValueError — Incompatible input shapes: axis values 14 (at axis 1) != 16 (at axis 1). Full input shapes: (None, 14), (None, 16) |
| [Course 3 - Unsupervised Learning, Recommenders, Reinforcement Learning/Week 3/Week 3 Programming Assignment/C3_W3_A1_Assignment.ipynb](Course%203%20-%20Unsupervised%20Learning%2C%20Recommenders%2C%20Reinforcement%20Learning/Week%203/Week%203%20Programming%20Assignment/C3_W3_A1_Assignment.ipynb) | 练习未完成 | 单元格 24：AssertionError — Wrong number of layers. Expected 3 but got 0 |
