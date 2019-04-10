import numpy as np
import matplotlib.pyplot as plt
import math


j = np.complex(0, 1)
pi = np.pi
e = np.e

def get_ak(x):
    a = []
    N = len(x)
    for k in range(int(-N/2),int(N/2)+1, 1):
        temp = 0
        for n in range(N):
            temp += x[n]*(e**(-1*j*k*2*pi*n/N))
        temp = temp/N
        a.append(temp)
    return a


x = input("enter your function : ").split()
y=[]
for i in x :
  y.append(float(i))

a = get_ak(y)

x = np.arange(int(-len(y)/2),int(len(y)/2)+1, 1)
plt.stem(x, np.real(a))
