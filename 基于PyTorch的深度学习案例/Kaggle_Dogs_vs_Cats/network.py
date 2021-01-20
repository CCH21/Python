import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data


"""
1.输入层Input：输入200×200的彩色图像，以RGB格式解析，为200×200×3的矩阵。（将图片送入网络前须将其调整为200×200）
2.卷积层Conv1：卷积核规模为3×3×3×16，即size为3×3，深度为3，数量为16。第一次卷积结果为16个feature map，200×200像素。
3.池化层Pooling：采用2×2的Max Pooling。第一次池化后，图像缩小为100×100像素。
4.卷积层Conv2：卷积核规模为3×3×16×16。即size为3×3，深度为16，数量为16。第二次卷积结果为16个feature map，100×100像素。
5.池化层Pooling：采用2×2的Max Pooling。第二次池化后，图像缩小为50×50像素。
6.全连接层FC1：输入为50×50×16的矩阵，输出为128×1的矩阵。首先将输入矩阵展开成50×50×16=40000的一维列向量，然后将每个数据对128个输出数据做映射，
  共40000×128=5120000个映射关系，每个映射需要一个权重系数。
7.全连接层FC2：将128维列向量映射至64维列向量。
8.全连接层FC3：将64维列向量映射至2维列向量。
9.输出层Output。
"""


# 新建网络类，继承PyTorch的nn.Module父类
class Net(nn.Module):
    # 设定网络层
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 16, 3, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, padding=1)
        self.fc1 = nn.Linear(50 * 50 * 16, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 2)

    # 重写父类forward方法，前向计算
    def forward(self, x):
        x = self.conv1(x)  # 第一次卷积
        x = F.relu(x)  # 第一次卷积结果使用ReLU激活函数处理
        x = F.max_pool2d(x, 2)  # 第一次池化
        x = self.conv2(x)  # 第二次卷积
        x = F.relu(x)  # 第二次卷积结果使用ReLU激活函数处理
        x = F.max_pool2d(x, 2)  # 第二次池化
        x = x.view(x.size()[0], -1)  # 将输入全连接层的[50*50*16]格式展开成[40000*1]的一维张量
        x = F.relu(self.fc1(x))  # 第一次全连接，使用ReLU函数激活
        x = F.relu(self.fc2(x))  # 第二次全连接，使用ReLU函数激活
        x = self.fc3(x)  # 第三次全连接
        return F.softmax(x, dim=1)  # 将输出值调整至[0.0, 1.0]，二者之和为1
