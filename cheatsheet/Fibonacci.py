# 다이나믹 programming

d = [0] * 100


# recursion
def fibo(x):
  if x == 1 or x == 2:
    return 1

  if d[x] != 0:
    return d[x]

  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

# for in loop
def fibo_for(x):
  d[1] = 1
  d[2] = 1
  n = 99

  for i in range(3, n-1):
    d[i] = d[ i-1 ] + d[ i-2 ]

  