import numpy as np
import os
from PIL import Image
import torch
import torch.utils.data as data
import torchvision.transforms as transforms


# 输入网络的图片大小
IMAGE_H = 200
IMAGE_W = 200

# 定义转换关系，将图像数据转换为Tensor形式，并且数值归一化到[0.0, 1.0]
data_transform = transforms.Compose([
    transforms.ToTensor()
])


# 新建数据集类，继承PyTorch的data.Dataset父类
class DogsVsCatsDataset(data.Dataset):
    def __init__(self, mode, Dir):
        self.mode = mode
        self.list_img = []                  # 存放图片路径
        self.list_label = []                # 存放图片对应标签，其中0表示猫，1表示狗
        self.data_size = 0                  # 记录数据集大小
        self.transform = data_transform     # 转换关系
        # 训练模式，需要提取图片路径和标签
        if self.mode == 'train':
            Dir += '/train/'
            for file in os.listdir(Dir):
                self.list_img.append(Dir + file)
                self.data_size += 1
                name = file.split(sep='.')  # 分割文件名
                if name[0] == 'cat':
                    self.list_label.append(0)
                else:
                    self.list_label.append(1)
        # 测试模式，只需要提取图片路径，标签设置为2，实际无意义
        elif self.mode == 'test':
            Dir += '/test/'
            for file in os.listdir(Dir):
                self.list_img.append(Dir + file)
                self.data_size += 1
                self.list_label.append(2)
        else:
            print('None')

    # 重载data.Dataset父类方法，获取数据集中数据内容
    def __getitem__(self, item):
        # 训练模式，需要读取数据集的image和label
        if self.mode == 'train':
            img = Image.open(self.list_img[item])
            img = img.resize((IMAGE_H, IMAGE_W))
            img = np.array(img)[:, :, :3]
            label = self.list_label[item]
            return self.transform(img), torch.LongTensor([label])
        # 测试模式，只需要读取数据集的image
        elif self.mode == 'test':
            img = Image.open(self.list_img[item])
            img = img.resize((IMAGE_H, IMAGE_W))
            img = np.array(img)[:, :, :3]
            return self.transform(img)
        else:
            print('None')

    # 返回数据集大小
    def __len__(self):
        return self.data_size
