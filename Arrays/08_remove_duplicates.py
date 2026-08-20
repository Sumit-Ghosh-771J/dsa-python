"""
8. Remove duplicates
"""

arr=list(map(int,input("Enter your elements: ").split()))
if len(arr)>0:
    j=0
    for i in range (1,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j]=arr[i]

    arr=arr[:j+1]
print(f"{arr}")
