#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# 导入数据集
data = pd.read_csv('./数据/20200515海外疫情情况.csv', encoding='gbk')
X = np.arange(1, 110).reshape((109, 1))
y = data['确诊人数']

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 训练分割后得到的训练集
regr = DecisionTreeRegressor(max_depth=10)
regr.fit(X_train, y_train)

# 用训练后的模型预测测试集结果
score = regr.score(X_test, y_test)
print(score)
