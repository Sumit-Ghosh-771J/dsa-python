"""
3. Find the 3rd Largest Number
"""

arr=list(map(int,input("Enter the elements u want to add: ").split()))

x=(float('-inf'))
y=(float('-inf'))
z=(float('-inf'))

for i in arr:
    if i>x:
        z=y
        y=x
        x=i
    elif i>y and i!=x:
        z=y
        y=i
    elif i>z and i!=y and i!=x:
        z=i
if z==(float('-inf'))
    print("Invalid")
else:
    print(f"Third largeat no. is: {z}")
