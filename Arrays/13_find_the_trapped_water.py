"""
13. Find the Trapped Water
"""

arr=list(map(int,input("Enter the elements u want to add: ").split()))
i=0
j=(len(arr)-1)
k=0
l=0
x=0
while i<j:

    if arr[i]>k:
        k=arr[i]
    if arr[j]>l:
        l=arr[j]
    if k>l:
        x+=l-arr[j]
        j-=1

    else:
        x+=k-arr[i]
        i+=1


print(f"{x}")
