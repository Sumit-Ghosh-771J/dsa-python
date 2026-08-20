"""
12. Find the highest possible area of the rectangle using 2 numbers from the array
"""

arr=list(map(int,input("Enter the elements u want to add: ").split()))

j=len(arr)-1
i=0
x=0

while i<j:

    if arr[i]<=arr[j]:
        if (j-i)*arr[i]>x:
            x=(j-i)*arr[i]
        i+=1
    else:
        if(j-i)*arr[j]>x:
            x=(j-i)*arr[j]
        j-=1

print(f"{x}")
