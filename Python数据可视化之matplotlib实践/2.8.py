import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.random.randn(1000)

# 函数boxplot()用于绘制箱线图
plt.boxplot(x)
"""
函数功能：
绘制箱线图
调用签名：
plt.boxplot(x)
参数说明：
x：绘制箱线图的输入数据
"""

plt.xticks([1], ["随机数生成器AlphaRM"])
plt.ylabel("随机数值")
plt.title("随机数生成器抗干扰能力的稳定性")

plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)

plt.show()
