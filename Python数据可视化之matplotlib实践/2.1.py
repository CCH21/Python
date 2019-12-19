import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# create bar
# 函数bar()用于绘制柱状图
plt.bar(x, y, align="center", color="c", tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")
"""
函数功能：
在x轴上绘制定性数据的分布特征
调用签名：
plt.bar(x, y)
参数说明：
x：标示在x轴上的定性数据的类别
y：每种定性数据的类别的数量
"""

# set x, y_axis label
plt.xlabel("箱子编号")
plt.ylabel("箱子重量(kg)")

plt.show()
