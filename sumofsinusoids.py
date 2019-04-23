import numpy as np
import matplotlib.pyplot as plot
def sine1(x,y,z):
	amplitude=np.cos((t*y)+z)
	d=x*amplitude
	return d
t=np.arange(0,10,0.1);
a1=input('enter first signal amplitude')
a2=input('enter second signal amplitude')
w1=input('enter first signal frequency')
w2=input('enter second signal frequency')
phase1=input('enter first signal phase')
phase2=input('enter second signal phase')
x1=sine1(a1,w1,phase1)
x2=sine1(a2,w1,phase1)
q=x3+x4
x5=sine1(a1,w1,phase1)
x6=sine1(a1,w1,phase2)
r=x5=x6
plot.subplot(3,1,1)
plot.plot(t,p)
plot.subplot(3,1,2)
plot.plot(t,q)
plot.subplot(3,1,3)
plot.plot(t,r)
plot.show()
