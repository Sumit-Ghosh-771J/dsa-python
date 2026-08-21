"""
11. Two sum
"""

#Updated

arr=list(map(int,input("Enter your elements: ").split()))
trgt=int(input("Enter the targeted no.: "))
arr.sort()
i=0
j=len(arr)-1
x=[]
while i<j:
    sum=arr[i]+arr[j]
    if sum == trgt:
        x.append((arr[i],arr[j]))
        j-=1
        i+=1
        while i<j and arr[i]==arr[i-1]:
            i+=1
        while i<j and arr[j]==arr[j+1]:
            j-=1
    elif sum<trgt:
        i+=1
    else:
        j-=1


print(f"{x}")
