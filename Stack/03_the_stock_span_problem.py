"""
3. The stock span problem
"""

mrp=list(map(int,input("Enter the elements: ").split()))
st=[]
span=[1]*len(mrp)

for i in range(len(mrp)):
    while st and mrp[st[-1]]<=mrp[i]:
        st.pop()
    if st:
        span[i]=i-st[-1]
    else:
        span[i]=i+1
    st.append(i)
print(span)
