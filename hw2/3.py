import numpy as np
import matplotlib.pyplot as plot


n = int(input("number of elements : "))
f={}
for i in range(n):
  x = float(input("x : "))
  y = float(input("y: "))
  f.update({x:y})
f2={}
for i in f:
  if -i not in f :
    f2.update({-i:0.0})

f2.update(f)
del f
f3={}

for i in f2:
  f3.update({i:f2.get(-i),-i:f2.get(i)})

f_odd={}
f_even={}
for i in f2 :
  f_odd.update({i:(f2.get(i) - f3.get(i))/2})
  f_even.update({i:(f2.get(i) + f3.get(i))/2})
f_odd.update({0.0:0.0})



plot.subplot(3,1,1)
plot.stem(f2.keys(),f2.values())
plot.title("function")


plot.subplot(3,1,2)
plot.stem(f_odd.keys(),f_odd.values())
plot.title("odd")
plot.subplots_adjust(top = 3)


plot.subplot(3,1,3)
plot.stem(f_even.keys(),f_even.values())
plot.title("even")
