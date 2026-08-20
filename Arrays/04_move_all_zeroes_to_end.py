"""
4. Move all zeroes to end
"""

arr=list(map(int,input("Enter the elements: ").split()))

z=0

for i in range (len(arr)):
    if arr[i]!=0:
        arr[z],arr[i]=arr[i],arr[z]
        z+=1

print(f"Array: {arr}")
