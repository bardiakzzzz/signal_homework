import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5, 5, 15)
x2 = np.linspace(-10, 10, 1000)

y1 =  np.cos(x1 * 9) + np.sin(2 * np.pi * x1)
y2 =  np.cos(x2 * 9) + np.sin(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.stem(x1, y1, '-')
plt.subplot(2, 1, 2)
plt.plot(x2, y2, '-')
