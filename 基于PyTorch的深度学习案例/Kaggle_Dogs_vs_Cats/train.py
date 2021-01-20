import torch
from torch.autograd import Variable
import torch.nn as nn
from torch.utils.data import DataLoader as DataLoader

from getData import DogsVsCatsDataset as DVCD
from network import Net


dataset_dir = './data/'
model_cp = './model/'
workers = 10               # PyTorch读取数据线程数量
batch_size = 16
lr = 0.0001                # 学习率


def train():
    datafile = DVCD('train', dataset_dir)
    dataloader = DataLoader(datafile, batch_size=batch_size, shuffle=True, num_workers=workers)

    print('Dataset loaded. Length of training set is {}.'.format(len(datafile)))

    model = Net()
    model = model.cuda()
    model.train()          # 网络设定为训练模式，采用dropout策略，可以防止网络过拟合

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)    # 实例化一个优化器，调整网络参数，优化方式为Adam方法
    criterion = nn.CrossEntropyLoss()    # 定义交叉熵损失函数

    cnt = 0                # 训练图片数量

    # 读取数据集中数据进行训练
    for img, label in dataloader:
        img, label = Variable(img).cuda(), Variable(label).cuda()
        out = model(img)   # 计算网络输出值，输出猫和狗的概率，调用了forward()方法
        loss = criterion(out, label.squeeze())    # 计算损失
        loss.backward()    # 误差反向传播，采用求导的方式计算网络中每个结点参数的梯度，梯度越大说明参数设置越不合理，需要调整
        optimizer.step()   # 采用设定的优化方法调整网络参数
        optimizer.zero_grad()    # 清除优化器中的梯度以便下一次计算
        cnt += 1
        print('Frame {}, Train Loss {}'.format(cnt * batch_size, loss / batch_size))

    torch.save(model.state_dict(), '{}/model.pth'.format(model_cp))    # 保存网络参数


if __name__ == '__main__':
    train()
