"""
20. Maximum of all sub-arrays of size k
"""

arr=list(map(int,input("Enter the elements: ").split()))
k=int(input("Enter the window size: "))
q=[]
ans=[]
for i in range(k):
    while q and arr[q[-1]]<arr[i]:
        q.pop(-1)
    q.append(i)
ans.append(arr[q[0]])
for i in range(k,len(arr)):
    if q and q[0]<=i-k:
        q.pop(0)
    while q and arr[q[-1]]<arr[i]:
        q.pop(-1)
    q.append(i)
    if q:
        ans.append(arr[q[0]])

print(ans)
