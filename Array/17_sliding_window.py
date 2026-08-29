"""
17. Sliding Window
"""

def sld_wind(ar,x):
    crntsm=sum(ar[:x])
    mxsm=crntsm
    for i in range(x,len(ar)):
        crntsm=crntsm-ar[i-x]+ar[i]
        if crntsm>mxsm:
            mxsm=crntsm
    return mxsm
arr=list(map(int,input("Enter the elements of the array: ").split()))
y=int(input("Enter the window size: "))
if len(arr)<y:
    print("Error! less than 3 elements entered")
else:
    res=sld_wind(arr,y)
    print(res)
