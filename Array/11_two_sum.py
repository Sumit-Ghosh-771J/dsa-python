"""
11. Find 2 numbers from whose sum is the targeted input number
"""

arr=list(map(int,input("Enter your elements: ").split()))
trgt=int(input("Enter the targeted no.: "))

i=0
j=len(arr)-1
x=[]
while i<j:
    sum=arr[i]+arr[j]
    if sum == trgt:
        x.append((i,j))
        i+=1
        j-=1
    elif sum<trgt:
        i+=1
    else:
        j-=1

print(f"INDEX{x}")
