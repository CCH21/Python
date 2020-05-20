#!/usr/bin/env python3

import graphviz
import numpy as np
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# 导入红酒数据集
wine = load_wine()
X = wine.data
y = wine.target

# 使用随机森林方法
# rfc = RandomForestClassifier()
# # 网格搜索找出最优参数
# # 字典param_grid给出参数可能的取值
# param_grid = {
#     'n_estimators': np.arange(10, 201, 10),
#     'max_features': np.arange(0.1, 1, 0.1),
#     'max_depth': np.arange(3, 13),
#     'bootstrap': [True, False]
# }
# # 进行网格搜索
# grid = GridSearchCV(rfc, param_grid=param_grid, cv=5)
# # 训练数据集
# grid.fit(X, y)
# # 输出最优参数的params, score, estimator
# print(grid.best_params_)
# print(grid.best_score_)
# print(grid.best_estimator_)
##################################################################################
# 得到结果如下：
# {'bootstrap': False, 'max_depth': 10, 'max_features': 0.1, 'n_estimators': 20}
# 0.9942857142857143
# RandomForestClassifier(bootstrap=False, ccp_alpha=0.0, class_weight=None,
#                        criterion='gini', max_depth=10, max_features=0.1,
#                        max_leaf_nodes=None, max_samples=None,
#                        min_impurity_decrease=0.0, min_impurity_split=None,
#                        min_samples_leaf=1, min_samples_split=2,
#                        min_weight_fraction_leaf=0.0, n_estimators=20,
#                        n_jobs=None, oob_score=False, random_state=None,
#                        verbose=0, warm_start=False)
##################################################################################

# 使用随机森林方法
# 参数为经过网格搜索后得出的最优参数
rfc = RandomForestClassifier(bootstrap=False, ccp_alpha=0.0, class_weight=None,
                             criterion='gini', max_depth=10, max_features=0.1,
                             max_leaf_nodes=None, max_samples=None,
                             min_impurity_decrease=0.0, min_impurity_split=None,
                             min_samples_leaf=1, min_samples_split=2,
                             min_weight_fraction_leaf=0.0, n_estimators=20,
                             n_jobs=None, oob_score=False, random_state=None,
                             verbose=0, warm_start=False)

# 训练数据集
rfc.fit(X, y)

# 绘制决策树
# 避免出现报错AttributeError: 'RandomForestClassifier' object has no attribute 'tree_'
rfc_tree = rfc.estimators_[0]
dot_data = tree.export_graphviz(rfc_tree, out_file=None, feature_names=wine.feature_names,
                                class_names=wine.target_names, filled=True, rounded=True, special_characters=True)
grap = graphviz.Source(dot_data)
grap.render('wine_网格追踪法')
