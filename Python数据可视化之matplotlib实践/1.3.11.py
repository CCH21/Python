import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

# 函数legend()标示不同图形的文本标签图例
plt.legend(loc="lower left")
"""
调用签名：
plt.legend(loc="lower left")
参数说明：
loc：图例在图中的地理位置
"""

plt.show()
