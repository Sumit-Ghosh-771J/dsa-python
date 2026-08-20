"""
15. Swap an array of 4 elements
"""

arr=list(map(int,input("Enter 4 no. separated by space: ").split()))
arr[0],arr[3]=arr[3],arr[0]
print(f"Your reversed array is: {arr}")
