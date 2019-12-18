import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)

# 函数scatter()寻找变量之间的关系
plt.scatter(x, y, label="scatter figure")
"""
调用签名：
plt.scatter(x, y, c="b", label="scatter figure")
参数说明：
x：x轴上的数值
y：y轴上的数值
c：散点图中标记的颜色
label：标记图形内容的标签文本
"""

plt.legend()

plt.show()
