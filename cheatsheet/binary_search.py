# 재귀로 구현한 이진 탐색

def binary_search(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    binary_search(array, target, start, mid)
  else:
    binary_search(array, target, mid+1, end)


# 반복문으로 구현한 이진 탐색
def bin_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1