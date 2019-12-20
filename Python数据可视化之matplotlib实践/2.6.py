import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

a = np.random.randn(100)
b = np.random.randn(100)


# colormap:RdYlBu
# 函数scatter()用于绘制气泡图
plt.scatter(a, b, s=np.power(10*a+20*b, 2),
            c=np.random.rand(100),
            cmap=mpl.cm.RdYlBu,
            marker="o")
"""
函数功能：
二位数据借助气泡大小展示三维数据
调用签名：
plt.scatter(x, y)
参数说明：
x：x轴上的数值
y：y轴上的数值
s：散点标记的大小
c：散点标记的颜色
cmap：将浮点数映射成颜色的颜色映射表
"""

plt.show()
