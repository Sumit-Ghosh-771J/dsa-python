"""
9. Find the missing number from the range of an array
"""

arr=list(map(int,input("Enter your elements(starting from 0): ").split()))
print(f"Missing no. from range {min(arr)}-{len(arr)} is : {(len(arr)*(len(arr)+1))//2-sum(arr)}")
