import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = 3 * np.sin(x*np.pi) + 3 * np.absolute(np.cos(7*x))

plt.subplot(1, 2, 1)
plt.plot(x,y,'-')
plt.title("Old")
for i in range (0,len(y),1) :
  if y[i] > 5 :
    y[i] = 5
  elif y[i] < 0:
    y[i] = 0
plt.subplot(1, 2, 2)
plt.plot(x, y, '-')
plt.title("New")
plot.show()
