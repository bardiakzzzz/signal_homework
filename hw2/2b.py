import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5, 5, 15)
x2 = np.linspace(-10, 10, 500)

y1 = np.absolute(np.sin(x1 * 2 * np.pi /3 )) + np.cos(x1 * 4 * np.pi / 3)
y2 = np.absolute(np.sin(x2 * 2 * np.pi /3 )) + np.cos(x2 * 4 * np.pi / 3)

plt.subplot(2, 1, 1)
plt.stem(x1, y1, '-')
plt.subplot(2, 1, 2)
plt.plot(x2, y2, '-')
