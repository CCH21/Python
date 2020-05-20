#!/usr/bin/env python3

import numpy as np
from sklearn.cluster import KMeans


def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(',')
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1, len(items))])
    return retData, retCityName


# 加载数据
data, cityName = loadData('./聚类/31省市居民家庭消费水平-city.txt')
# 创建K-means算法实例，并进行训练，获得标签
km = KMeans(n_clusters=5)     # 聚成5类
label = km.fit_predict(data)
expenses = np.sum(km.cluster_centers_, axis=1)
# print(expenses)
CityCluster = [[], [], [], [], []]
for i in range(len(cityName)):
    CityCluster[label[i]].append(cityName[i])
for i in range(len(CityCluster)):
    print('Expenses: %.2f' % expenses[i])
    print(CityCluster[i])
