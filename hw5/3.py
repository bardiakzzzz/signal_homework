import numpy as np
import matplotlib.pyplot as plt
import math


j = np.complex(0, 1)
pi = np.pi
e = np.e

def a():
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-1,1,1):
            if k==0:
                temp += 0
            else:
                temp += (np.sin(2*pi/3)*k-np.sin(pi/3)*k)*(e**(j*2*pi*pi*n/3))/(pi*k)
        y.append(temp)
    return y

def b():
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-2,2,1):
            if k==0:
                temp += 0
            else:
                temp += (np.sin(2*pi/3)*k-np.sin(pi/3)*k)*(e**(j*k*6*n))/(pi*k)
        y.append(temp)
    return y

def c():
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-5,5,1):
            if k==0:
                temp += 0
            else:
                temp += (np.sin(2*pi/3)*k-np.sin(pi/3)*k)*(e**(j*k*6*n))/(pi*k)
        y.append(temp)
    return y

def d():
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-10,10,1):
            if k==0:
                temp += 0
            else:
                temp += (np.sin(2*pi/3)*k-np.sin(pi/3)*k)*(e**(j*k*6*n))/(pi*k)
        y.append(temp)
    return y


x1 = a()
x2 = b()
x3 = c()
x4 = d()

x = np.arange(-10,10,0.001)

plt.subplot(5,1,1)
plt.plot(x, np.real(x1))
plt.subplot(5,1,2)
plt.plot(x, np.real(x2))
plt.subplot(5,1,3)
plt.plot(x, np.real(x3))
plt.subplot(5,1,4)
plt.plot(x, np.real(x4))
