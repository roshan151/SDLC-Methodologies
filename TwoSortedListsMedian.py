l1 = input("Enter first array")
l2 = input("Enter second array")
L1=l1.split(',')
L2=l2.split(',')
A1=[]
A2=[]
#Code to convert string numbers to integers
for i in L1:
    A1.append(int(i))
for i in L2:
    A2.append(int(i))
n=len(A1)
m=len(A2)
i=0
j=0
#Code to merge both lists
while i<n and j<m:
    if A1[i]>=A2[j]:
        A1.insert(i,A2[j])
        j=j+1
        n=n+1
    i=i+1
if j<m-1:
    A1 = A1[:] + A2[j:]
print('Merged numbers',A1)
#Code to find median of the merged lists
n=len(A1)
if (n%2==0):
    m=int(n/2)
    median=(A1[m]+A1[m-1])/2
else:
    m=int((n+1)/2)
    median=A1[m-1]
print('Median is:',median)
