"""
1. Next greater element using monotonic stack
"""

arr = list(map(int, input("Enter the elements: ").split()))

stack = []
ans = [-1] * len(arr)  # Pre-fill with -1 assuming no greater element exists

# Walk backwards through the array: right to left
for i in range(len(arr) - 1, -1, -1):

  # 1. Throw away shorter people sitting to the right (they get blocked)
  while stack and stack[-1] <= arr[i]:
    stack.pop()

  # 2. If someone taller is left on the stack, that's our Next Greater Element!
  if stack:
    ans[i] = stack[-1]

  # 3. Add current element to the stack so elements to the left can see it
  stack.append(arr[i])

print(ans)
