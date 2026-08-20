"""
10. List to Set
"""

x=[]
n=int(input("Enter the no of elements: "))
for i in range (n):
 num=int(input(f"Enter the {i+1} element: "))
 x.append(num)
y=list(set(x))
print(y)
print("Greatest no.: ",max(y))
print("Smallest no.: ",min(y))
