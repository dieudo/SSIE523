from pylab import *

Dt = 0.01

def initialize():
    global x, xresult, y, yresult
    x = y = 0.1
    xresult = [x]
    yresult = [y]
    
def observe():
    global x, xresult, y, yresult
    xresult.append(x)
    yresult.append(y)

a=1; b=1.5; c=0.5; d=1; J=1; K=4
def update():
    global x, xresult, y, yresult
    nextx = x + (a*x*(1-x/K)-b*J*x/(J+x)*y) * Dt
    nexty = y + (-c*y+d*J*x/(J+x)*y) * Dt
    x, y = nextx, nexty

def plot_phase_space():
    initialize()
    for t in xrange(100000):
        update()
        observe()
    plot(xresult, yresult)
    #axis('image')
    #axis([-3, 3, -3, 3])
    title('d = ' + str(d))

values = arange(0.7, 0.9, .02)
for i in xrange(len(values)):
    subplot(1, len(values), i + 1)
    d = values[i]
    plot_phase_space()

show()