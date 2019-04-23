import numpy as np
import cmath as cm
from matplotlib import pyplot as plt
x=input ("enter the sequence")
l=len(x)
j=cm.sqrt(-1)
y=[ ]
for k in range(0,l-1):
    sum=0
    for n in range(0,l):
     sum=sum+(x[n]*(np.exp((-j)*(2*np.pi/l)*n*k)))
    y=np.append(y,sum)
m=y/l
print (m)
plt.stem(np.abs(y))
plt.show()