"""
15. Closest 3 sum
"""

def three_sm(ar,xx):
    n=len(ar)
    ar.sort()
    closest=ar[0]+ar[1]+ar[2]

    for i in range(n-2):
        if ar[i]>0 and ar[i]==ar[i-1] :
            continue
        l=i+1
        r=n-1
        while l<r:
            sm=ar[i]+ar[l]+ar[r]
            z=sm-xx
            if abs(closest-xx)>(sm-xx):
                closest=sm
            if sm == xx:
                return sm
            elif sm<xx:
                l+=1
            else:
                r-=1

    return closest
arr=list(map(int,input("Enter the elements you want to add: ").split()))
a=int(input("Enter the target number u want 3 nos. from the array sum upto: "))
result=three_sm(arr,a)
print(result)
