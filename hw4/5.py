import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1,5,5)

x1 = [0, 2, 2, 2, 0]
h1 = [0, 1, -1, 0, 0]
h2 = [0, 0, 1, -1, 0]
h = [0, 1, 0, -1, 0]

r1 = np.convolve(x1, h1)
r2 = np.convolve(x1, h2)
r = []

for i in range (len(h1)):
  r.append(h1[i] + h2[i])

y = np.convolve(x1, h)

plot.subplots_adjust(hspace = 1)
plt.subplot(3,1,1)
plt.title('x')
plt.stem(x, signal)

plt.subplot(3,1,2)
plt.title('h')
plt.stem(x, h)

t =  np.linspace(1,9,9)
plt.subplot(3,1,3)
plt.title('y')
plt.stem(t,y)
