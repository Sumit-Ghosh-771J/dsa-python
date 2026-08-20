"""
6. User Dictionary
"""

dict={}
n=int(input("Enter no. of elements: "))
for i in range(n):
 key=input(f"Enter {i+1} key: ")
 val=input(f"Enter '{key}' value/name: ")
 dict[key]=val
print("\nYour Dictionary")
print(dict)
