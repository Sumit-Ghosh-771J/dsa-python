"""
7. Find the unique item
"""

arr = list(map(int, input("Enter your elements: ").split()))

# Step 1: Build frequency dictionary
counts = {}

for num in arr:
    if num in counts:
        counts[num] += 1   # Increment count if we've seen it before
    else:
        counts[num] = 1    # Set initial count to 1 for new numbers

# Step 2: Collect keys that appeared exactly once
result = []

for num in counts:
    if counts[num] == 1:
        result.append(num)

print(f"The unique numbers are: {result}")
