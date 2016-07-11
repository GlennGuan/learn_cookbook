#. 在不同的容器中进行迭代。

# itertools.chain() 接受一系列可迭代对象作为输入并返回一个迭代器。
# 对多个容器进行迭代。
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
	print(x)

# chain()常见的用途是想一次性对所有的元素执行某项特定的操作，但是这些元素分散在不同的集合中。

active_items =set()
inactive_items = set()

for item in chain(active_items, inactive_items):
	# Process item

for x in a + b:  # a+b产生新序列，a和b还要同一类型
	...

for x in chain(a, b):  # 序列很大的话，在内存使用上高效很多
	...
