"""
12. List to Tuple
"""

x=[]
n=int(input("Enter the no of elements: "))
for i in range (n):
 z=(input(f"Enter the {i+1} element: "))
 if z.isdigit(): # Checks if int or alpha
  val=int(z)
  x.append(val)
 else:
  x.append(z)
y=tuple(set(x))
print(y)
print(type(y))
print(type(x[0]))
