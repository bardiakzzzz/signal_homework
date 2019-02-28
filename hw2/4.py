import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5,5, 21)
x2 = np.linspace(-5, 5, 1000)

y1 = np.cos((np.pi * x1 / 3)  + np.pi/4)
z1 = 2 * (np.e)**(x1)
w1 =  2 * (np.e)**(x1)*(np.cos((np.pi * x1 / 3)  + np.pi/4))

y2 = np.cos((np.pi * x2 / 3)  + np.pi/4)
z2 = 2 * (np.e)**(x2)
w2 =  2 * (np.e)**(x2)*(np.cos((np.pi * x2 / 3)  + np.pi/4))


plt.subplot(3, 2, 1)
plt.stem(x1, y1, '-')
plt.subplot(3, 2, 3)
plt.stem(x1, z1, '-')
plt.subplot(3, 2, 5)
plt.stem(x1, w1, '-')

plt.subplot(3, 2, 2)
plt.plot(x2, y2, '-')
plt.subplot(3, 2, 4)
plt.plot(x2, z2, '-')
plt.subplot(3, 2, 6)
plt.plot(x2, w2, '-')


plt.show()
