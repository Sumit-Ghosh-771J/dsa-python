def check_even_odd(a):
 if a%2==0:
  return 'even'
 else:
  return 'odd'


x=int(input("Enter a no.: "))
main=check_even_odd(x)
print(f"The no. is {main}")
