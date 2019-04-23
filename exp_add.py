import numpy as np
import matplotlib.pyplot as plt
n=10
x=[]
for i in range(n):
	a=np.exp(i)
	x.append(a)
print(x)
y=[]
for i in range(n):
	b=np.exp(i)
	y.append(b)
print(y)
z=[]
for i in range(n):
	s=x[i]*y[i]
	z.append(s)
print(z)
plt.subplot(311)
plt.plot(x)
plt.subplot(312)
plt.plot(y)
plt.subplot(313)
plt.plot(z)
plt.show()
	
