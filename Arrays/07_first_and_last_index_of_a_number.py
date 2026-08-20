"""
7. First and Last index of a number
"""

arr=list(map(int,input("Enter your elements: ").split()))
x=int(input("Enter the targeted no.: "))
first=-1
last=-1

for i in range (len(arr)):
    if arr[i]==x:
        if first == -1:
            first=i
        last=i

if first!=-1:
    print(f"First index:{first}\nLast index:{last}")
else:
    print("Not found")
