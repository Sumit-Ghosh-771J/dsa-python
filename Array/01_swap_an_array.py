"""
1. Swap an Array
"""

arr=list(map(int,input("Enter the elements separated by space: ").split()))

l=0
r=len(arr)-1

while l<r:
    arr[l],arr[r]=arr[r],arr[l]

    l+=1
    r-=1

print(f"{arr}")
