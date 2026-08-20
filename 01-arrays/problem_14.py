"""
13. String Operation
"""

x=input("Enter a word: ").strip()
z=x.lower()
y=z[ : :-1]#reversing a word
if y==z:
 print(f" {x} is a palindrome")
else:
 print(f" {x} is not a palindrome")
print(x.upper())# turns into capital letters
print(x.lower())# turns into small letters
print(x[1:4:1])# [start:stop:step]
print(x[ :3: ])# stops at index 3(index 3 excluded)
print(x[3: : ])# starts from index 3(index 3 included)
print(x[ : :2])# used to jump between characters(default settings is 1)
print(x.strip())# removes spaces
print(x.isdigit())# checks is digit
print(x.isalpha())# checks if alphabet
split=x.split(",")# converts string to list
print(split)
join=("-").join(split)# converts list to string
print(join)
