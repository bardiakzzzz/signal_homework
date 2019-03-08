import matplotlib.pyplot as plot
import numpy as np


x = np.linspace(-20,20, 41)
x2 = np.linspace(-20,20, 100)

y1 = np.cos(6*x/7)

y2 = np.cos(2 * np.pi * x2) + 1j * np.sin(np.pi * x2)



plot.subplots_adjust(hspace = 1)
plot.subplot(2,1,1)
plot.stem(x,y1)
plot.title("function 1")


plot.subplot(2,1,2)
plot.plot(x2,y2,'-')
plot.title("function 2")
