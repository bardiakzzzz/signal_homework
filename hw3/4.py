import matplotlib.pyplot as plot
import numpy as np



m = int(input("m : "))

x = np.linspace(-5,5, 11)
x1=[]
for i in x :
  x1.append(i/m)

y = np.sin(2 * np.pi * 0.043 * x) + np.sin(2 * n * 0.031 * n)

plot.subplot(2,1,1)
plot.stem(x, y,'-')

plot.subplot(2,1,2)
plot.stem(x1, y,'-')
