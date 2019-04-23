import numpy as np
import matplotlib.pyplot as plot
f1=input("enter first sinusoid")
f2=input("enter second sinusoid")
fs=input("enter sampling frequncy")
n=np.arange(0,1000,10);
x1=np.cos(2*(3.14)*(f1/fs)*n)
x2=np.cos(2*(3.14)*(f2/fs)*n)
x=x1+x2
plot.subplot(3,1,1)
plot.plot(n,x1,'g')
plot.subplot(3,1,2)
plot.plot(n,x2,'b')
plot.subplot(3,1,3)
plot.plot(n,x,'r')
plot.grid(True,which='both')
plot.title('sum of two sinusoids')
plot.show()
