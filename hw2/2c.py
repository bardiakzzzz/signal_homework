import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5, 5, 15)
x2 = np.linspace(-20, 20,100)

y1 = np.sin(13 * (np.pi/3) * x1)
y2 = np.sin(13 * (np.pi/3) * x2)

plt.subplot(2, 1, 1)
plt.stem(x1, y1, '-')
plt.subplot(2, 1, 2)
plt.plot(x2, y2, '-')
