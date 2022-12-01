# 시뮬레이션 문제의 유형 중 맵을 생성해서 경로를 확인해야 하는 문제 (DFS/BFS)가 아닌 경우
n,m = map(int, input().split())
x,y,direction = map(int, input().split())

# 방문 위치를 저장하기 위한 2차원 배열을 작성. 맵으로 활용한다.
d = [[0] * m for _ in range(n)]
# 초기 위치를 저장한다.
d[x][y] = 1

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 1. 이동 패턴을 저장한다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0

while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if d[x][y] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue

  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0:
      x= nx
      y= ny
    
    else:
      break
    turn_time = 0

print(count)

