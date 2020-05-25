#!/usr/bin/env python3

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer                # 预处理模块
from sklearn.utils import shuffle                       # 将训练数据打乱
from sklearn.metrics import classification_report       # 预测结果评估模块
from sklearn.neighbors import KNeighborsClassifier      # K近邻分类器
from sklearn.tree import DecisionTreeClassifier         # 决策树分类器
from sklearn.naive_bayes import GaussianNB              # 高斯朴素贝叶斯函数


def load_dataset(feature_paths, label_paths):
    """
    读取特征文件列表和标签文件列表中的内容，归并后返回
    :param feature_paths:特征文件列表
    :param label_paths:标签文件列表
    :return:特征集合和标签集合
    """
    # 定义feature数组变量，列数量和特征维度一致为41
    feature = np.ndarray(shape=(0, 41))
    # 定义空的标签变量，列数量和标签维度一致为1
    label = np.ndarray(shape=(0, 1))

    for file in feature_paths:
        # 使用逗号分隔符读取特征数据，将问号替换标记为缺失值，文件中不包含表头
        df = pd.read_table(file, delimiter=',', na_values='?', header=None)
        # 使用平均值补全缺失值，然后将数据进行补全
        imp = SimpleImputer(missing_values=np.NaN, strategy='mean', verbose=0)
        imp.fit(df)
        df = imp.transform(df)
        # 将新读入的数据合并到特征集合中
        feature = np.concatenate((feature, df))

    for file in label_paths:
        # 读取标签数据，文件中不包含表头
        df = pd.read_table(file, header=None)
        # 将新读入的数据合并到标签集合中
        label = np.concatenate((label, df))
    # 将标签规整为一维向量
    label = np.ravel(label)
    return feature, label


if __name__ == '__main__':
    # 设置数据路径
    feature_paths = ['./分类/dataset/A/A.feature', './分类/dataset/B/B.feature', './分类/dataset/C/C.feature',
                     './分类/dataset/D/D.feature', './分类/dataset/E/E.feature']
    label_paths = ['./分类/dataset/A/A.label', './分类/dataset/B/B.label', './分类/dataset/C/C.label',
                   './分类/dataset/D/D.label', './分类/dataset/E/E.label']

    # 将前4个数据作为训练集读入
    x_train, y_train = load_dataset(feature_paths[:4], label_paths[:4])
    # 将最后1个数据作为测试集读入
    x_test, y_test = load_dataset(feature_paths[4:], label_paths[4:])
    # 使用shuffle函数将训练数据打乱
    x_train, y_train = shuffle(x_train, y_train)

    # 创建K近邻分类器，并在测试集上进行预测
    print('Start training knn')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done!')
    answer_knn = knn.predict(x_test)
    print('Prediction done!')

    # 创建决策树分类器，并在测试集上进行预测
    print('Start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done!')
    answer_dt = dt.predict(x_test)
    print('Prediction done!')

    # 创建贝叶斯分类器，并在测试集上进行预测
    print('Starting training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done!')
    answer_gnb = gnb.predict(x_test)
    print('Prediction done!')

    # 计算准确率与召回率
    print('\n\nThe classification report for knn:')
    print(classification_report(y_test, answer_knn))
    print('\n\nThe classification report for dt:')
    print(classification_report(y_test, answer_dt))
    print('\n\nThe classification report for gnb:')
    print(classification_report(y_test, answer_gnb))
