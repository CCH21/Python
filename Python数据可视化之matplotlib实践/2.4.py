import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

kinds = "简易箱", "保温箱", "行李箱", "密封箱"

colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]

soldNums = [0.05, 0.45, 0.15, 0.35]

# pie chart
# 函数pie()用于绘制饼图
plt.pie(soldNums,
        labels=kinds,
        autopct="%3.1f%%",
        startangle=60,
        colors=colors)
"""
函数功能：
绘制定性数据的不同类别的百分比
调用签名：
plt.pie(x)
参数说明：
x：定性数据的不同类别的百分比
"""

plt.title("不同类型箱子的销售数量占比")

plt.show()
