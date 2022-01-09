st=input('Enter comma seperated numbers')
k=int(input('Enter k'))
t=int(input('Enter t'))
num=st.split(',')
nums=[int(x) for x in num]
so=nums[:]
so.sort()
def position(n,m,nums,q=0):

    if q!=0:
        num = nums[:]
        i=0
        pos_lis=[]
        while q!=0:
            pos1=num.index(n)
            pos_lis.append(pos1)
            num[pos1]='null'
            i=i+1
        print(pos_lis)
        return pos_lis
    else:
        pos1=nums.index(n)
        pos2=nums.index(m)
        return abs(pos1-pos2)
i=0
z=0
ans=False
while i+1<len(so):
    j=i+1
    if j<len(so) and so[j]==so[i]:
        z=j
        n=so[i]
        m=so[j]
        while z<len(so) and so[z]==so[i]:
            so[z]='null'
            z=z+1
        pos_lis=position(n,m,nums,z)
        for i in pos_lis:
            j=i
            while j<len(pos_lis):
                if abs(i-pos_lis[j])<=k:
                    ans=True
                    break
            if ans==True:
                break
    else:
        while j<len(so) and so[j]-so[i]<=t:
            ch = position(so[i],so[i+1],nums)
            print(so[i],so[i+1],ch)
            if ch<=k:
                ans=True
                break
            j=j+1
    i=i+1
print(ans)

