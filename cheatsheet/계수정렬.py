array = [1,2,3,4,5,6,7]

count = [0] * (len(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(len(count[i])):
    print(i, end=' ')