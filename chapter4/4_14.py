#. 扁平化处理嵌套性的序列 p138

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types): # 检查某个元素是否可迭代，和不是字符串》。
			yield from flatten(x)  # 将可迭代对象作为一种例程进行递归，
		else:
			yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
	print(x)


# 不用yield from 用for循环

def flatten(items, ignore_types):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types): 
			for i in flatten(x):
				yield i
			else:
				yield x

# ...哪个好？
