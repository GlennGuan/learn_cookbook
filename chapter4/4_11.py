#. 同时迭代多个序列

xpts = [1, 5, 4, 2, 9, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
	print(x, y)

# zip(a, b) 创建一个迭代器，可产生元祖（x, y),x取值序列a, y取值序列b。
# 迭代长度以最短序的长度列为准

a = [1, 2, 3]
b = ['w', 'x', 'z', 'a', 'o']
for i in zip(a,b):
	print(i)

# 以上行为不是所需：itertools.zip_longest()
from itertools import zip_longest
for i in zip_longest(a, b):
	print(i)

s = dict(zip(b, a))
for name, val in zip(b, a):
	print(name, '=', val)

b = [4,5,6]
c = [7,8,9]
for i in zip(a, b, c):
	print(i)

# zip()的结果是一个迭代器， 可用list将数据存为列表
