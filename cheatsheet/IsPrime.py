import math

def isPrime(x):
  for i in range(2, int(math.sqrt(x) + 1)):
    if x % i == 0:
      return False
  return True


# 에라토스테네스의 체 : 여러개의 수가 소수인지 판별하는 알고리즘

# 1. n+1 크기의 True list를 선언
n = 1000
array = [True for i in range(n+1)]

# 2. 2부터 n의 제곱근까지 모든 수를 확인하여 남아있는 i를 제외한 모든 배수 지우기
for i in range(2, int(math.sqrt(n) + 1)): 
  if array[i] == True: 
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1
# 3. 판별된 소수를 출력
  for i in range(2, n+1):
    if array[i]:
      print(i, end=' ')


# n = 1000 ==> 2부터 1000까지 모든 수에 대해 소수판별
def eratos(n):
  array = [True for i in range(n+1)]

  for i in range(2, int(math.sqrt(n) + 1)):
    if array[i] == True:
      iternum = 2
      while i * iternum <= n:
        array[i*iternum] = False
        iternum += 1

    for i in range(2,n+1):
      if array[i]:
        print(i, end=' ')

