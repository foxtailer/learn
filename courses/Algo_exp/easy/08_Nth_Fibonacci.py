#  O(n^2) time | O(n) space
def get_nth_fib(n):
  if n == 2:
    return 1
  elif n == 1:
    return 0
  else:
    return get_nth_fib(n-1) + get_nth_fib(n-2)


#  O(n) time | O(n) space
def get_nth_fib2(n, memoize={1:0, 2:1}):
  if n in memoize:
    return memoize[n]
  else:
    memoize[n] = get_nth_fib2(n-1, memoize) + get_nth_fib2(n-2, memoize)
    return memoize[n]
  

#  O(n) time | O(1) space
def get_nth_fib3(n):
  last_two = [0, 1]
  counter = 3

  while counter <= n:
    last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
    counter += 1

  return last_two[1] if n > 1 else last_two[0]  

print(get_nth_fib(7), get_nth_fib2(7), get_nth_fib3(7), sep='*')