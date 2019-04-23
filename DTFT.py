import numpy as np
import cmath as cm
import matplotlib.pyplot as plt
def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(0,2*np.pi,N)
	for i in range(0,N):
		w=p[i]
		sum=0
		for k in range(0,n):
			sum=sum+x[k]*np.exp(-j*w*k)
		y.append(abs(sum))
	return y
x=(input('enter seq='))
t=dtft(x)
plt.plot(t)
plt.show( )
	
