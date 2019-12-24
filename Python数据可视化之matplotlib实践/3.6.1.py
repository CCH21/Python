import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6, 1)
y = [0, 4, 3, 5, 6]
y1 = [1, 3, 4, 2, 7]
y2 = [3, 4, 1, 6, 5]

labels = ["BluePlanet", "BrownPlanet", "GreenPlanet"]
colors = ["#8da0cb", "fc8d62", "#66c2a5"]

# 函数stackplot()绘制堆积折线图
plt.stackplot(x, y, y1, y2, labels=labels, colors=colors)

plt.legend(loc="upper left")

plt.show()
