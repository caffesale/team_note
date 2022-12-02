array = [1,5,6,8,3,5,6,3,2]


def qsort(array, start, end):
  if start > end:
    return
  # 첫 피벗은 스타트지점
  pivot = start
  left = start + 1
  right = end
  while left < right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
      
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1
    # 엇갈렸으면 작은 데이터와 피벗을 교체
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[pivot] = array[pivot], array[left]
  
  qsort(array, start, right - 1)
  qsort(array, right + 1, end)


# 파이썬식으로 작성한 퀵 정렬 
def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

