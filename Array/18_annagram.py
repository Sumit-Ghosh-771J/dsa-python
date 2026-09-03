"""
18. Annagram
"""

arr = list(input("Enter the elements you want to add: "))
pat = list(input("Enter the pattern: "))

k = len(pat)
ans = 0

count = {}
check = {}

for i in range(k):
  char_p = pat[i]
  count[char_p] = count.get(char_p, 0) + 1

  char_a = arr[i]
  check[char_a] = check.get(char_a, 0) + 1

if check == count:
  ans += 1

for i in range(k, len(arr)):
  out_char = arr[i - k]
  check[out_char] -= 1
  if check[out_char] == 0:
    del check[out_char]

  in_char = arr[i]
  check[in_char] = check.get(in_char, 0) + 1

  if check == count:
    ans += 1

print("Total Anagrams:", ans)
