from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['a','b','c']

result = list(permutations(data,2))

result2 = list(combinations(data,2))
result3 = list(product(data, repeat=2))
result4 = list(combinations_with_replacement(data, 2))


print(result) 
# permutations
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

print(result2)
# combinations 
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

print(result3)
# product
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

print(result4)
# combinations_with_replacement
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

