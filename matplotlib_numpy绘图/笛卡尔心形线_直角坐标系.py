import numpy
import matplotlib.pyplot as plt

a = 1
t = numpy.linspace(0, 2 * numpy.pi, 1024)
X = a * (2 * numpy.cos(t) - numpy.cos(2 * t))
Y = a * (2 * numpy.sin(t) - numpy.sin(2 * t))
plt.plot(Y, X, color='r')
plt.show()
