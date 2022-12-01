import heap

# 최소 힙
def heapsort(iterable):
  h = []
  result = []

  for value in iterable:
    heapq.heappush(h, value)
    # 최대 힙은 힙에 삽입할 때 -value

  for _ in range(len(h)):
    result.append(heapq.heappop(h))
    # 최대 힙은 힙에 pop할 때 -heapq.headpop(h)
  return result

result = heapsort([1,3,4,5])

print(result)