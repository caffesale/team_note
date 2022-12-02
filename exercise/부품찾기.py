# 이진 탐색으로 풀기

def bin_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n = int(input())
items = list(map(int, input().split()))
items.sort()

m = int(input())
req = list(map(int, input().split()))

for it in req:
  result = bin_search(items, it, 0, n-1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')


# 계수 정렬로 풀기

n = int(input())
items = list(map(int, input().split()))

m = int(input())
req = list(map(int, input().split()))

count = [0] * (len(items) + 1)

for i in range(len(items)):
  count[items[i]] += 1


for it in req:
  if array[it] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')

# 집합 자료형으로 풀기

n = int(input())
items = set(map(int, input().split()))

m = int(input())
req = list(map(int, input().split()))

for it in req:
  if it in items:
    print