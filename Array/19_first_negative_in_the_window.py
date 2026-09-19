"""
19. First negative in the window
"""

arr=list(map(int,input("Enter the elements: ").split()))
k=int(input("Enter the window size: "))
q=[]
ans=[]
for i in range(k):
    if arr[i]<0:
        q.append(i)
if q:
    ans.append(arr[q[0]])
else:
    ans.append(0)
for i in range(k,len(arr)):
    if q and q[0]<=i-k:
        q.pop(0)
    if arr[i]<0:
        q.append(i)
    if q:
        ans.append(arr[q[0]])
    else:
        ans.append(0)
print(ans)
