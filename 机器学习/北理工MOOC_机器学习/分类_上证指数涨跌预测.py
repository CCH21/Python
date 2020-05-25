#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split

# 数据加载和预处理
data = pd.read_csv('./分类/stock/000777.csv', encoding='gbk', parse_dates=[0], index_col=0)
data.sort_index(0, ascending=True, inplace=True)
# 选取5列数据作为特征（收盘价，最高价，最低价，开盘价，成交量）
# 选取150天的数据
dayfeature = 150
featurenum = 5 * dayfeature
# x记录150天的5个特征值，y记录涨跌情况
x = np.zeros((data.shape[0] - dayfeature, featurenum + 1))
y = np.zeros((data.shape[0] - dayfeature))
for i in range(data.shape[0] - dayfeature):
    x[i, 0:featurenum] = np.array(data[i:i + dayfeature]
                                  [[u'收盘价', u'最高价', u'最低价', u'开盘价', u'成交量']]).reshape((1, featurenum))
    # 最后一列记录当日的开盘价
    x[i, featurenum] = data.loc[:, u'开盘价'].iloc[i + dayfeature]
for i in range(data.shape[0] - dayfeature):
    if data.loc[:, u'收盘价'].iloc[i + dayfeature] >= data.loc[:, u'开盘价'].iloc[i + dayfeature]:
        y[i] = 1
    else:
        y[i] = 0

# 创建SVM并进行交叉验证
# 核函数为rbf
clf = svm.SVC(kernel='rbf')
rbf_result = []
for i in range(5):
    # 将80%的数据作为训练集，20%的数据作为测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # 训练数据
    clf.fit(x_train, y_train)
    rbf_result.append(np.mean(y_test == clf.predict(x_test)))
print('SVM classifier accuacy - rbf:')
print(rbf_result)
# 核函数为sigmoid
clf = svm.SVC(kernel='sigmoid')
sigmoid_result = []
for i in range(5):
    # 将80%的数据作为训练集，20%的数据作为测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # 训练数据
    clf.fit(x_train, y_train)
    sigmoid_result.append(np.mean(y_test == clf.predict(x_test)))
print('SVM classifier accuacy - sigmoid:')
print(sigmoid_result)
