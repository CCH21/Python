#!/usr/bin/env python3

from sklearn.datasets import load_wine
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# 导入红酒数据集
wine = load_wine()
X = wine.data
y = wine.target

# 使用弱学习方法
clf = DecisionTreeClassifier(random_state=0)

# 通过bagging将给定的弱学习方法学习n次
bagging = BaggingClassifier(clf, max_samples=0.5, max_features=0.5, n_estimators=200)

# K折交叉验证
# 验证clf
score1 = cross_val_score(clf, X, y, cv=5)
print(score1)
# 验证bagging
score2 = cross_val_score(bagging, X, y, cv=5)
print(score2)
