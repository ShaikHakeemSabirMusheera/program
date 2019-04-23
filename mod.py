import numpy as np
import matplotlib.pyplot as plt
def dft(x):
	X=[]
	mag=[]
	phase=[]
	for k in range(len(x)-1):
		s=0
		for n in range(len(x)-1):
			s+=x[n]*np.exp(-2*1j*np.pi*k*n/(len(x)))
		X.append(s)
		mag.append(abs(X[k]))
		phase.append(np.angle(X[k]))
	return X
n=input("Enter number of samples:")
x=[]
for i in range(n):
	a=input("Enter the samples:")
	x.append(a)
print(x)
X=[]
X=dft(x)
#print(X)
y=[]
f0=10
Fs=100
N=50
for i in range(500):
	a=np.cos(2*np.pi*f0*i*Fs/N)
	y.append(a)
#print(y)
Y=[]
Y=dft(y)
#print(Y)
plt.subplot(211)
plt.stem(X)
plt.subplot(212)
plt.stem(Y)
plt.show()
'''
z=[]
for i in range(n):
	d=x[i]*y[i]
	z.append(d)
print(z)
'''
