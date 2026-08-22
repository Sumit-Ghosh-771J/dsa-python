"""
15. Closest 3 sum
"""

def three_sum(ar,xx):
    n=len(ar)
    if n<3:
        return "Need atleast  3 elements"
    ar.sort()
    closest=ar[0]+ar[1]+ar[2]

    for i in range(n-2):

        if i>0 and ar[i]==ar[i-1] :
            continue
        l=i+1
        r=n-1
        while l<r:
            sm=ar[i]+ar[l]+ar[r]
            if abs(closest-xx)>abs(sm-xx):
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
result=three_sum(arr,a)
print(result)
