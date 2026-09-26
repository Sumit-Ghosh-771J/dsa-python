"""
4. Largest area of rectangle possible
"""

arr=list(map(int,input("Enter the elements: "). split ()))
arr.append(0)
st=[]
h=0
w=0
area=0

for i in range(len(arr)):
    while st and arr[st[-1]]>=arr[i]:
        pop=st.pop()
        h=arr[pop]
        if st:
            w=i-st[-1]-1
        else:
            w=i

        area=max(area,h*w)
    st.append(i)
print(area)
