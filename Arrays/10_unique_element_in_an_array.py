"""
10. Unique Element in an Array
"""

arr=list(map(int,input("Enter your elements: ").split()))
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
result=[]
for i in count:
    if count [i]==1:
        result.append(i)
print(f"Unique element: {result}")
