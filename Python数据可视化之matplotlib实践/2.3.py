import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# set test scores
boxWeight = np.random.randint(0, 10, 100)

x = boxWeight

# plot histogram
bins = range(0, 11, 1)

# 函数hist()用于绘制直方图
plt.hist(x, bins=bins,
         color="g",
         histtype="bar",
         rwidth=1,
         alpha=0.6)
"""
函数功能：
在x轴上绘制定量数据的分布特征
调用签名：
plt.hist(x)
参数说明：
x：在x轴上绘制箱体的定量数据输入值
"""

# set x, y-axis label
plt.xlabel("箱子重量(kg)")
plt.ylabel("销售数量（个）")

plt.show()
