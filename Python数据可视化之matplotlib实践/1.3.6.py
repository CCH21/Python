import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

# 函数axhline()和axvline()绘制平行于x轴和y轴的水平参考线
plt.axhline(y=0.0, c="r", ls="--", lw=2)
"""
调用签名：
plt.axhline(y=0.0, c="r", ls="--", lw=2)
参数说明：
y：水平参考线的出发点
c：参考线的线条颜色
ls：参考线的线条风格
lw：参考线的线条宽度
平移性：上面的函数功能，调用签名和参数说明同样可以平移到函数axvline()上
"""
plt.axvline(x=4.0, c="r", ls="--", lw=2)

plt.show()
