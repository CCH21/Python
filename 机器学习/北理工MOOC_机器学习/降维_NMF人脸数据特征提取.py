#!/usr/bin/env python3

import matplotlib.pyplot as plt
from numpy.random import RandomState
from sklearn import decomposition
from sklearn.datasets import fetch_olivetti_faces

# 设置基本参数并加载数据
n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data


# 设置图像的展示方式
def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    # 创建图片，并指定图片大小（英寸）
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    # 设置标题及字号大小
    plt.suptitle(title, size=16)
    for i, comp in enumerate(images):
        # 选择画制的子图
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        # 对数值归一化，并以灰度图形式显示
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray, interpolation='nearest', vmin=-vmax, vmax=vmax)
        # 去除子图的坐标轴标签
        plt.xticks(())
        plt.yticks(())
    # 对子图位置及间隔调整
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.93, 0.04, 0.)


# 创建特征提取的对象NMF，使用PCA作为对比
estimators = [
    ('Eigenfaces - PCA using randomized SVD', decomposition.PCA(n_components=6, whiten=True)),
    ('Non-negative components - NMF', decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3))
]

# 降维后数据点的可视化
for name, estimator in estimators:
    print("Extracting the top %d %s..." % (n_components, name))
    print(faces.shape)
    estimator.fit(faces)
    components_ = estimator.components_
    plot_gallery(name, components_[:n_components])
plt.show()
