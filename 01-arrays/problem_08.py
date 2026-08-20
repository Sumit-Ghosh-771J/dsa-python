"""
8. Function
"""

def add_numbers(a, b):
    result = a + b  #local variable
    return result  # Sends the calculated value back

# Store the returned value in a variable  # Global variable (keyword to force local variable in function to be global is 'global')
x,y=map(int,input("Enter 2 no. separated by space: ").split())
total = add_numbers(x,y)

print(f"The total is: {total}") # Output: The total is: 30
