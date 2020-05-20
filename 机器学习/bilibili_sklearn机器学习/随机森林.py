#!/usr/bin/env python3

import graphviz
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# 导入红酒数据集
wine = load_wine()
X = wine.data
y = wine.target

# 使用随机森林方法
rfc = RandomForestClassifier(random_state=0, n_estimators=200)

# K折交叉验证
score = cross_val_score(rfc, X, y, cv=5)
print(score)

# 训练数据集
rfc.fit(X, y)

# 绘制决策树
# 避免出现报错AttributeError: 'RandomForestClassifier' object has no attribute 'tree_'
rfc_tree = rfc.estimators_[0]
dot_data = tree.export_graphviz(rfc_tree, out_file=None, feature_names=wine.feature_names,
                                class_names=wine.target_names, filled=True, rounded=True, special_characters=True)
grap = graphviz.Source(dot_data)
grap.render('wine')
