import matplotlib.pyplot as plot
import numpy as np
from scipy import signal



x = np.linspace(-20,20, 41)

y = x
y1=[]
y2=[]
y3=[]
z1=[]
z2=[]
z3=[]
z4=[]
z5=[]
for i in y :
  if (i >= 0) :
    y1.append(1)
    z1.append(i)
  else:
    y1.append(0)
    z1.append(0)
for i in y :
  if (i >= 12) :
    y2.append(1)
    z3.append(i-12)
  else:
    y2.append(0)
    z3.append(0)

for i in y :
  if(i >= 4):
    z2.append(i-4)
  else:
    z2.append(0)

for i in y :
  if(i >= 16):
    z4.append(i-16)
  else:
    z4.append(0)


for i in range(len(y1)):
  y3.append(y1[i]-y2[i])
  z5.append(z1[i]-z2[i]-z3[i]+z4[i])

y = np.array(y3)
z = np.array(z5)

plot.subplots_adjust(hspace = 1)
plot.subplot(3,1,1)
plot.stem(x,y3)
plot.title("function 1")

plot.subplot(3,1,2)
plot.stem(x,z5)
plot.title("function 2")

u = signal.deconvolve(y,z)[0]



plot.subplot(3,1,3)
plot.stem(x,u)
plot.title("deconvolved")
