#!/usr/bin/env python3

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 给定数据集
# 训练集
data = pd.read_csv('./数据/20200515海外疫情情况.csv', encoding='gbk')
# print(data)
X = np.arange(1, 110).reshape((109, 1))
y = data['确诊人数']
# 给定测试集的X
X_test = np.arange(1, 141).reshape((140, 1))

# 实例化
regr_1 = DecisionTreeRegressor(max_depth=4)    # max_depth为最大拟合深度
regr_2 = DecisionTreeRegressor(max_depth=10)

# 训练
regr_1.fit(X, y)
regr_2.fit(X, y)

# 根据训练结果，传入测试集，令其预测y的取值
y1 = regr_1.predict(X_test)
y2 = regr_2.predict(X_test)

# 绘制折线图
plt.plot(np.arange(1, 110), data['确诊人数'], label='实际确诊')
plt.plot(np.arange(1, 141), y1, label='预测确诊1')
plt.plot(np.arange(1, 141), y2, label='预测确诊2')
plt.legend()
plt.show()
