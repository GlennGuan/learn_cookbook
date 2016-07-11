# 实现迭代协议p118.

# Node类来表示树结构
# 实现一个迭代器能够以深度优先的模式遍历树的节点。
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

	def depth_first(self):
		yield self
		for c in self:
			yield from c.depth_first()

# Example

if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	child1.add_child(Node(3))
	child1.add_child(Node(4))
	child2.add_child(Node(5))
	for ch in root.depth_first():
		print(ch)
	# 以上，depth_first()的实现非常易于阅读，秒速起来也很方便，
	# 首先产生自身，然后迭代每个子节点，利用子节点的depth_first()方法（通过yield from语句）昌盛出其他元素
