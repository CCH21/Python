#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# 导入数据集
iris = load_iris()
X = iris.data
y = iris.target

# 验证决策树分类模型
clf = DecisionTreeClassifier()

# 使用cross_val_score进行验证
score = cross_val_score(clf, X, y, cv=10)
print(score)
print(score.mean())
