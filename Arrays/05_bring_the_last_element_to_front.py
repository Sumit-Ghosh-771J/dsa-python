"""
5. Bring the last element to front
"""

arr=list(map(int,input("Enter ur elements: ").split()))
for i in range(len(arr)):
    arr[i],arr[len(arr)-1]=arr[len(arr)-1],arr[i]
print(f"{arr}")
