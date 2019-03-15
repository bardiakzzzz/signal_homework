import random
import numpy as np
import matplotlib.pyplot as plt



t = random.randint(3, 20)


x = np.linspace(0,t-1,t)

y = []
for i in range(0,t):
    y.append(random.randint(1, 100))


h = []
for i in range(0,t):
    h.append(0.25)

ans = np.convolve(y, h)

plt.subplot(3,1,1)
plt.stem(x,y)

plt.subplot(3,1,2)
plt.stem(x,h)

plt.subplot(3,1,3)
x = np.linspace(0, 2*t-1, 2*t-1)
plt.stem(x,ans)
