import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

# 函数text()添加图形内容细节的无指向性注释文本
plt.text(3.10, 0.09, "y=sin(x)", weight="bold", color="b")
"""
调用签名：
plt.text(x, y, string, weight="bold", color="b")
参数说明：
x：注释文本内容所在位置的横坐标
y：注释文本内容所在位置的纵坐标
string：注释文本内容
weight：注释文本内容的粗细风格
color：注释文本内容的字体颜色
"""

plt.show()
