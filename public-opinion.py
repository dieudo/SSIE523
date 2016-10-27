from pylab import *
def init():
    global x, y, xdata, ydata
    x=.1; y=.101; xdata=[x]; ydata=[y]
def observe():
    global xdata, ydata
    xdata.append(x); ydata.append(y)
def update():
    global x, y
    nx = min([x-y+1,1])*x \
      + (max([1-exp(1-x/y),0]))*(1-x)
    ny = min([y-x+1,1])*y \
      + (max([1-exp(1-y/x),0]))*(1-y)
    x, y = nx, ny
init()
for t in range(30):
    update()
    observe()
plot(xdata); plot(ydata)