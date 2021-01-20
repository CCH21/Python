import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import torch
from torch.autograd import Variable

from getData import DogsVsCatsDataset as DVCD
from network import Net


dataset_dir = './data'
model_file = './model/model.pth'


def test():
    model = Net()
    model.cuda()
    model.load_state_dict(torch.load(model_file))
    model.eval()    # 网络设定为评估模式，计算过程中不需dropout

    datafile = DVCD('test', dataset_dir)    # 实例化一个数据集
    print('Dataset loaded. Length of test set is {}.'.format(len(datafile)))

    index = np.random.randint(0, datafile.data_size, 1)[0]    # 随机从数据集中获取一个测试图片
    img = datafile.__getitem__(index)
    img = img.unsqueeze(0)
    img = Variable(img).cuda()
    out = model(img)
    print(out)    # 输出该图像属于猫或狗的概率
    if out[0, 0] > out[0, 1]:    # 属于猫的概率大于属于狗的概率
        print('The image is a cat.')
    else:                        # 属于狗的概率大于属于猫的概率
        print('The image is a dog.')

    img = Image.open(datafile.list_img[index])
    plt.figure('Test Image')
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    test()
