#!/usr/bin/env python3

import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans


# 加载图片并进行预处理
def loadData(filePath):
    f = open(filePath, 'rb')
    data = []
    # 以列表形式返回图片像素值
    img = image.open(f)
    # 获得图片的大小
    m, n = img.size
    # 将每个像素点RGB颜色处理到0-1范围内并存放进data
    for i in range(m):
        for j in range(n):
            x, y, z = img.getpixel((i, j))
            data.append([x / 256.0, y / 256.0, z / 256.0])
    f.close()
    # 以矩阵形式返回data以及图片大小
    return np.mat(data), m, n


# 加载训练数据
imgData, row, col = loadData('./基于聚类的整图分割/bull.jpg')

# 加载K-means聚类算法
km = KMeans(n_clusters=3)           # 聚类中心的个数为3

# 对像素点进行聚类并输出
# 聚类获得每个像素所属的类别
label = km.fit_predict(imgData)
label = label.reshape([row, col])
# 创建一张新的灰度图保存聚类后的结果
pic_new = image.new('L', (row, col))
# 根据所属类别向图片中添加灰度值
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j), int(256 / (label[i][j] + 1)))
# 以JPEG格式保存图像
pic_new.save('./基于聚类的整图分割/result_bull.jpg', 'JPEG')
