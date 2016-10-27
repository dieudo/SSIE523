import matplotlib
matplotlib.use('TkAgg')
from pylab import *
n = 100; p = 0.5; r = 1
def initialize():
    global C, nextC
    C = zeros([n,n])
    nextC = zeros([n,n])
    for x in xrange(n):
        for y in xrange(n):
            C[x,y] = 1 if random() < p else 0
def observe():
    global C
    cla()
    imshow(C, interpolation='none',
           cmap = cm.binary, vmin = 0, vmax = 1)
def update():
    global C, nextC
    for x in xrange(n):
        for y in xrange(n):
            count = 0
            for dx in range(-r, r+1):
                for dy in range(-r, r+1):
                    count += C[(x+dx)%n,(y+dy)%n]
            if C[x,y] == 0:
                nextC[x,y] = 1 if count == 3 else 0
            else:
                nextC[x,y] = 1 if 3 <= count <= 4 else 0
    nextC, C = C, nextC
    
import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])