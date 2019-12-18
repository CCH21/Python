import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)     # linspace(0.05, 10, 1000)表示在0.05至10之间均匀地取1000个数
y = np.cos(x)

# 函数plot()展现变量的趋势变化
plt.plot(x, y, ls="-", lw=2, label="plot figure")
"""
调用签名：
plt.plot(s, y, ls="-", lw=2, label="plot figure")
参数说明：
x：x轴上的数值
y：y轴上的数值
ls：折线图的线条风格
lw：折线图的线条宽度
label：标记图形内容的标签文本
"""

plt.legend()        # legend()标示不同图形的文本标签图例

plt.show()
