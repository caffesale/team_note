

def factorization(x):
  result = []
  i = 2
  while i <= x:
    if x % i == 0:
      result.append(i)
      x //= i
    else:
      i += 1