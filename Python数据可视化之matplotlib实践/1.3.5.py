import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

# 函数grid()绘制刻度线的网格线
plt.grid(linestyle=":", color="r")
"""
调用签名：
ply.grid(linestyle=":", color="r")
参数说明：
linestyle：网格线的线条风格
color：网格线的线条颜色
"""

plt.show()
