# 데이터가 거의 정리되어 있을 때 더 빠른 알고리즘
array = [1,5,6,8,3,5,6,3,2]

for i in range(len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
