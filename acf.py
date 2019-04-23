from matplotlib import pyplot as plt
import numpy as np
x=np.array(input("enter the seq1:"))
h=x
def rev(x):
	n=len(x)
	j=n-1
	i=0
	temp=0
	y=[]
	p=[]
	while(i<j):
		temp=x[i]
		y[i]=x[j]
		x[j]=temp
		i+=1
		j-=1
		l=np.append(p,x)
	return l
a=rev(x)
def convolute(a,h):
	n1=len(a)
	n2=len(x)
	y=[  ]
	for n in range (n1+n2-1):
		sum=0
		for k in range(n1):
			if (n-k<n2 and n-k>=0):
				sum=sum+(x[k]*a[n-k])
		y=np.append(y,sum)
	return y
print convolute(a,x)
print a


