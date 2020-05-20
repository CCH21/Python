#!/usr/bin/env python3

import graphviz
from sklearn import datasets, tree

# 给定数据集
iris = datasets.load_iris()
# print(iris.feature_names)

# 实例化
clf = tree.DecisionTreeClassifier()  # 决策树的分类方法

# 训练数据集
clf.fit(iris.data, iris.target)

# 绘制决策树
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names,
                                filled=True, rounded=True, special_characters=True)
grap = graphviz.Source(dot_data)
grap.render('iris')
