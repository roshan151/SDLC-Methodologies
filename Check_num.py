#Checks if numbers are greater than a certain limit

rainfall_mi = input("Input string of numbers with ', ' to check")
k=float(input("Input the checkpoint number"))
l1=rainfall_mi.split(', ')
l1_bool=[float(x)>k for x in l1]
c=l1_bool.count(True)
print(c)
