# 321

s = input()

mid_index = len(s) // 2

left = s[:mid_index]
right= s[mid_index:]

n1 = 0
for l in left:
  n1 += int(l)

n2 = 0
for r in right:
  n2 += int(r)

if (n1 == n2) :
  print('LUCKY')
else:
  print('READY')