"""
16. Four sum
"""

arr=list(map(int,input("Enter the elements you want to add: ").split()))
x=int(input("Enter your target no.: "))
def four_sum(ar,trgt):
    n=len(ar)
    ar.sort()
    xx=[]
    for i in range (n-3):
        if i>0 and ar[i]==ar[i-1]:
            continue
        j=i+1
        for j in range(i+1,n-2):
            if j>i+1 and ar[j]==ar[j-1]:
                continue
            l=j+1
            r=n-1
            while l<r:
                sum=ar[i]+ar[j]+ar[l]+ar[r]
                if sum==trgt:
                   xx.append ((ar[i],ar[j],ar[l],ar[r]))
                   l+=1
                   r-=1
                   while l<r and ar[l]==ar[l-1]:
                         l+=1
                   while l<r and ar[r]==ar[r+1]:
                         r-=1
                elif sum<trgt:
                   l+=1
                else:
                   r-=1
    return xx
result=four_sum(arr,x)
if len(result)==0:
    print("No quadruplets found")
else:
    print(result)
