# 그래프는 인접 행렬, 인접 리스트로 표현할 수 있다.
# 파이썬에서는 둘 다 2차원 배열에 넣어 활용한다.

INF = 987654321


# matrixGraph[x][y]의 값으로 [x] 노드에서 [y]노드의 거리 표현
matrixGraph = [
  [0,7,5],
  [7,0,INF],
  [5,INF, 0]
]

listGraph = [[] for _ in range(3)]

# 인덱스 [0] 노드에서 1까지의 거리 7
# 인덱스 [0] 노드에서 2까지의 거리 5
listGraph[0].append((1,7))
listGraph[0].append((2,5))

