import numpy
import matplotlib.pyplot as plt

X = numpy.linspace(0, 2 * numpy.pi, 1024)
plt.axes(polar=True)
plt.plot(X, 1.-numpy.sin(X), color='r')
plt.show()
