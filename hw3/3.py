import matplotlib.pyplot as plot
import numpy as np



n = int(input("number of elements in first function  : "))
f={}
f2={}
for i in range(n):
  x = float(input("x : "))
  y = float(input("y: "))
  f.update({x:y})
print("f1 : ",f)
m = int(input("number of elements in second function  : "))
for i in range(m):
  x = float(input("x : "))
  y = float(input("y: "))
  f2.update({x:y})
print("f2 : ",f2)


plot.subplots_adjust(hspace = 1)
plot.subplot(3,1,1)
plot.stem(f.keys(),f.values())
plot.title("function 1")

plot.subplot(3,1,2)
plot.stem(f2.keys(),f2.values())
plot.title("function 2")

f3 = np.convolve(np.array(list(f.values())),np.array(list(f2.values())),'same')
plot.subplot(3,1,3)
plot.stem(f2.keys(),f3)
plot.title("convolved")
