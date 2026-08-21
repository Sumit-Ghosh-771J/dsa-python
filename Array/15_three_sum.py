"""
14. Three sum
"""

def three_sum(ar):
    ar.sort()
    n = len(ar)
    x=[]

    for i in range(n-2):
        if i > 0 and ar[i] == ar[i-1]:
            continue
        if ar[i] > 0:
            break
        l=i+1
        r=n-1
        while l < r:
            sum = ar[i]+ar[l]+ar[r]
            if sum == 0:
                x.append((ar[i], ar[l], ar[r]))
                l += 1
                r -= 1
                while l < r and ar[l] == ar[l-1]:
                    l += 1
                while l < r and ar[r] == ar[r+1]:
                    r -= 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return x

arr = list(map(int, input("Enter the elements u want to add: ").split()))
result=three_sum(arr)
if len(result)==0:
    print("No triplets found")
else:
    print(result)
