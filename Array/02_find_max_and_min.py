"""
2. Find Max and Min
"""

arr=list(map(int,input("Enter the no. u want to add to the list: ").split()))

min=arr[0]
max=arr[0]

for i in arr:
    if i<min:
        min=i
    if i>max:
        max=i
print(f"Maximum no. in list is: {max}\nMinimum no. in list is: {min}")
