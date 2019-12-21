import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# create bar
plt.bar(x, y, align="center", color="c", tick_label=["A", "B", "C", "D", "E"], hatch="///")
"""
关键字参数hatch设置柱体的填充样式
关键字参数hatch可以有很多取值，例如，“"/"” “"\\"” “"|"” “"-"”等
每种符号字符串都是一种填充柱体的几何样式
符号字符串的符号数量越多，柱体的几何图形的密集程度越高
"""

# set x, y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

plt.show()
