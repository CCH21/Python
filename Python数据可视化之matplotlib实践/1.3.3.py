import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)

plt.scatter(x, y, label="scatter figure")

plt.legend()

# 函数xlim()和ylim()设置x轴和y轴的数值显示范围
plt.xlim(0.05, 10)
"""
调用签名：
plt.xlim(xmin, xmax)
参数说明：
xmin：x轴上的最小值
xmax：x轴上的最大值
平移性：上面的函数功能，调用签名和参数说明同样可以平移到函数ylim()上
"""
plt.ylim(0, 1)

plt.show()
