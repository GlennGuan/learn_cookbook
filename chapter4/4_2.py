# 委托迭代 p118.
# 构建一个自定义的容器对象，其内部持有一个list tuple 和其他iterable对象
# 定义一个__iter__()方法，将迭代请求委托到对象内部持有的容器上。

class Node:
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return 'Node({!r})'.format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children) # 将迭代请求转发给对象内部持有的_children属性上。

# Example

if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	for ch in root:
		print(ch)

		# output Node(1), Node(2)

# iter(s)通过调用s.__iter__()来简单地返回底层的迭代器，len(s) s.__len__()

# 未完。。。
