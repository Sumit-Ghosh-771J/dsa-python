"""
2. Next warm day
"""

temp=list(map(int,input("Enter the elements : ").split()))
ans=[0]*len(temp)
st=[]

for i in range (len(temp)-1,-1,-1):
    while st and temp[st[-1]]<=temp[i]:
        st.pop()
    if st:
        ans[i]=st[-1]-i
    st.append(i)
print(ans)
