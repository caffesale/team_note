# 최단 탈출구를 구현하는 문제에서 사용한다. 

from collections import deque

def bfs(graph, start, visited):
  # 큐 구현
  queue = deque([start])

  # 현재 노드 방문처리
  visited[start] = True

  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드의 연결 정보를 2차원 배열로 표현
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)