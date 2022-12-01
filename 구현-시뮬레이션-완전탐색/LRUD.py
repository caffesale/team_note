# 계획서에 따라 이동하는 유형의 문제

n = int(input())
plans = input().split()
x,y = 1,1

# 이런 유형의 문제에서는 이동 계획에 따라 

# 1. 움직일 수 있는 경우의 수를 확인
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

# 2. 가상의 이동패턴이 유효한 지 확인하고 적용한다. 
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

    # 3. 이동패턴이 범위를 초과한다면 무효화, 혹은 이동패턴이 범위에 들어왔을 때만 이동을 적용한다.
    if nx < 1 or nx > n or ny < 1 or ny > n :
      continue
    x,y = nx,ny

print(x,y)

## dx = [], dy =[] 형 외에도 다른 해결방식이라면...

steps = [(-2,-1), (-1,-2), (1,-2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  # 범위에 들어왔을 때만 이동을 적용한다.
