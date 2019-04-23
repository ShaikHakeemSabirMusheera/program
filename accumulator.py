import numpy as np
import matplotlib.pyplot as plt
sample=input("enter numberof samples")
x=np.arange(sample)
y1=x*x
plt.plot(x,y1,'g')
plt.xlabel('sample(n)')
plt.ylabel('sample(v)')
s=[]
for in in range(0,sample):
	y1=i*i
	s.append(y1)
print (s)
len=len(s)
sum=[]
s2=0
for i in range(0,len):
	s2+=s[i]
	sum.append(s2)
plt.stem(i,sum)
plt.show()
