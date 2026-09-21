"""
20. Maximum of all sub-arrays of size k
"""

from collections import deque
arr=list(map(int,input("Enter the elements: ").split()))
k=int(input("Enter the window size: "))
q=deque()
ans=[]
for i in range(k):
    while q and arr[q[-1]]<arr[i]:
        q.pop()
    q.append(i)
ans.append(arr[q[0]])
for i in range(k,len(arr)):
    if q and q[0]<=i-k:
        q.popleft()
    while q and arr[q[-1]]<arr[i]:
        q.pop()
    q.append(i)
    if q:
        ans.append(arr[q[0]])

print(ans)
