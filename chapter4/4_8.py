# 跳过可地带对象中的前一部分元素.

from itertools import dropwhile
with open('./7_8.py') as f:
	for line in dropwhile(lambda line: line.startswith('#'),f):
		print(line, end='')


# 以上是根据测试函数的结果来跳过前面的元素
# 如果你知道跳过多少个元素，可以使用itertools.islice()

from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
	print(x)

# dropwhile(),islice(),避免写出以下代码
with open('./7_2.py') as f:

	while True:
		line = next(f, '')
		if not line.startswith('#'):
			break

# while line:
# 	print(line, end='')
# 	line = next(f, None)


# 第一个示例重写
with open('./7_3.py') as f:
	lines = (line for line in f if not line.startswith('#'))
	for line in lines:
		print(line, end='')
