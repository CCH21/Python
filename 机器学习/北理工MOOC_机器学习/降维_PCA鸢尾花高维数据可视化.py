#!/usr/bin/env python3

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# 已知鸢尾花数据是四维的，共三类样本
# 使用PCA实现对鸢尾花数据进行降维，实现在二维平面的可视化
# 加载数据并进行降维
data = load_iris()
y = data.target
X = data.data
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

# 按类别对降维后的数据进行保存
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
# 按照鸢尾花的类别将降维后的数据点保存在不同的列表中
for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])

# 降维后数据点的可视化
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()
