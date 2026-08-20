"""
4. List Operation
"""

x=[]
n=int(input("Enter the no. of elements: "))
for i in range(n):
  num=int(input(f"Enter the {i+1} element: "))
  x.append(num)
print(x)
print(max(x))
print(min(x))
print(len(x))
print(x[0])
print(x[-1])
print(sum(x))
