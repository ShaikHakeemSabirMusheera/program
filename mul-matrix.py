m=input("enter no of rows in a matrix")
n=input("enter no of columns in a matrix")
mat1=[]
for i in range(0,m):
	mat1.append([])
for i in range(0,m):
	for j in range(0,n):
		mat1[i].append(j)
		mat1[i][j]=0
		print("enter in row",i+1,"enter in column",j+1)
		mat1[i][j]=(input())
print mat1
p=input("enter no of rows in a matrix")
q=input("enter no of columns in a matrix")
mat2=[]
for i in range (0,p):
	mat2.append([])
for i in range(0,p):
	for j in range (0,q):
		mat2[i].append(j)
		mat2[i][j]=0
		print("enter in row",i+1,"column",j+1)
		mat2[i][j]=(input())
print(mat2)
res=[]
for i in range (0,m):
	res.append([])
for i in range (0,m):
	for j in range(0,q):
		res[i].append(j)
		res[i][j]=0
for p in range(len(mat1)):
	for q in range(len(mat2[0])):
		for r in range(len(mat2)):
			res[p][q]+=mat1[p][r]*mat2[r][q]
print(res)

