#. 迭代所有可能的组合或排列 p128

# 对一系列元素所有可能的组合或排列进行迭代。

items = ['a','b','c']
from itertools import permutations
for p in permutations(items):
	print(p)

# 较短的，所有全排列
for p in permutations(items, 2):
	print(p)

# 输入序列号中所有元素的全部组合形式
from itertools import combinations
for c in combinations(items, 3):
	print(c)

for c in combinations(items, 2):
	print(c)

for c in combinations(items, 1):
	print(c)

# 对于combinations()来说，组合（‘a','b')和('b','a')被认为是相同的组合形式。

# 当产生组合时，已经选择过的元素将从可能的候选元素中移除
# itertools.combinations_with_replacement()函数允许元素得到多次选择
import itertools
for c in itertools.combinations_with_replacement(items, 3):
	print(c)

