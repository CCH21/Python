#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('./数据/20200515海外疫情情况.csv', encoding='gbk')
X = np.arange(1, 110).reshape((109, 1))
y = data['确诊人数']

regr = DecisionTreeRegressor(max_depth=10)

score = cross_val_score(regr, X, y, cv=10, scoring='neg_mean_squared_error')
print(score)
