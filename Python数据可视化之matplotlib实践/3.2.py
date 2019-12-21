import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# create horizontal bar
plt.barh(x, y, align="center", color="b", tick_label=["A", "B", "C", "D", "E"])
"""
参数说明：
x：柱状图中的y轴上的柱体标签值
y：柱状图中的柱体宽度
align：柱体对齐方式
color：柱体颜色
tick_label：刻度标签值
"""

# set x, y_axis label
plt.ylabel("测试难度")
plt.xlabel("试卷份数")

# set xaxis grid
plt.grid(True, axis="x", ls=":", color="r", alpha=0.3)

plt.show()
