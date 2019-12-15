import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d

fig = plt.figure()
ax = plt.subplot(111, projection='3d')
ax.set_title('Gradient Descent', fontsize=16)
X = np.arange(-10, 10, 0.04)
Y = np.arange(-10, 10, 0.04)
X, Y = np.meshgrid(X, Y)
Z = (X ** 2 + Y ** 2 + X * Y + X + Y + 1)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
