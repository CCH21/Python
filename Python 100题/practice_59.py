import numpy as np
import matplotlib.patches as mpathes
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
xy = np.array([0, 0])
ellipse = mpathes.Ellipse(xy, 4, 2, color='c')
ax.add_patch(ellipse)

plt.axis('equal')
plt.show()
