"""
6. Check sorted or not
"""

def sort(ar):
    for i in range(len(ar)-1):
        if ar[i]>ar[i+1]:
            return False
    return True

arr=list(map(int,input("Enter your elements: ").split()))
if sort(arr)==True:
    print("Entered array is 'sorted'")
else:
    print("Entered array is 'not sorted'")
