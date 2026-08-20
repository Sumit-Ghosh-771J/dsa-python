"""
9. Set
"""

# 1. Initialize an empty set
user_set = set()

# 2. Ask how many elements
n = int(input("How many items do you want to add? "))

# 3. Add items using a loop
for i in range(n):
    val = int(input(f"Enter item {i + 1}: "))
    user_set.add(val)
# Uses .add() for sets!

print("\nFinal Unique Set:", user_set)
