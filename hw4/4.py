from scipy import signal
import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(-1,3,5)

y1 = [0,1,1,0,0]
x1 = [1,2,1,0,0]


u = signal.deconvolve(y1,x1)[1]

x2 = [0,2,3,0,-1]
y2 = np.convolve(x2,u,'same')


plot.subplots_adjust(hspace = 1)
plot.subplot(2,1,1)
plot.stem(x,u)
plot.title("deconvolved")


plot.subplot(2,1,2)
plot.stem(x,y2)
plot.title("result")
