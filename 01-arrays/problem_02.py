"""
2. Greater & Smaller
"""

a,b=map(int,input("Enter 2 no. separated by space: ").split())
if a<b:
 print(f"{b} is greater than {a}")
elif a>b:
 print(f"{a} is greater than {b}")
else :
 print("Both are equal")
