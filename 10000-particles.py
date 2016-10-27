import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 10000

def initialize():
    global xs, ys
    xs = [random() for i in xrange(n)]
    ys = [random() for i in xrange(n)]
    
def observe():
    global xs, ys
    cla()
    plot(xs, ys, 'o')
    axis('image')

def update():
    global xs, ys
    for i in xrange(n):
        th = uniform(-pi, pi)
        xs[i] += 0.05*cos(th)
        ys[i] += 0.05*sin(th)

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])