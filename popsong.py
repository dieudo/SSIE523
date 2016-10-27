from pylab import *
Dt = 0.001; a = b = c = 1.
def init():
    global p, pdata, q, qdata, t, tdata
    p=0.01; pdata=[p]; q=.5; qdata=[q]; t=0; tdata=[t]
def observe():
    global p, pdata, q, qdata, t, tdata
    pdata.append(p); qdata.append(q); tdata.append(t)
def update():
    global p, pdata, q, qdata, t, tdata
    np=p+(b*p-c*q*p)*Dt; nq=q+(a*p)*Dt
    # dp/dt = bp-cpq, dq/dt = ap
    p, q = np, nq; t += Dt
init()
while t < 10:
    update(); observe()
plot(tdata, pdata); plot(tdata, qdata)
    