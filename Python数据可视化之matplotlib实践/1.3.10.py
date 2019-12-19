import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

# 函数title()添加图形内容的标题
plt.title("y=sin(x)")
"""
调用签名：
plt.title(string)
参数说明：
string：图形内容的标题文本
"""

plt.show()
