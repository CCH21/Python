import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# create bar
plt.bar(x, y, align="center", color="b", tick_label=["A", "B", "C", "D", "E"], alpha=0.6)
"""
参数说明：
x：柱状图中的柱体标签值
y：柱状图中的柱体高度
align：柱体对齐方式
color：柱体颜色
tick_label：刻度标签值
alpha：柱体的透明度
"""

# set x, y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.show()
