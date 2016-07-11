# 反向迭代p121.

# 内建reversed()函数实现反向迭代

a = [1, 2, 3, 4]
for x in reversed(a):
	print(x)   # 4, 3, 2 ,1....

# 以上有个前提： 待处理对象拥有可确定的大小，或者对象实现了__reversed__()特殊方法时，才能奏效。
# 如果这两个条件都无法满足，则必须首先将这个对象转换为列表。

f = open('./7_1.py')
for line in reversed(list(f)):
	print(line, end="")
# 以上代码在当可迭代对象较大时，会消耗大量的内层。

# 定义一个反向迭代器，效率省内存。
class Countdown:
	def __init__(self, start):
		self.start = start
	# Forward iterator
	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1
	# Reverse iterator
	def __reversed__(self):  # __reversed__()方法实现反向迭代。
		n = 1
		while n <= self.start:
			yield n
			n += 1
