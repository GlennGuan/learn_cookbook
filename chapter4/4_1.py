# 手动访问迭代器中的元素.
# 处理某个可迭代对象中的元素，但是基于某种原因不能也不想使用for循环

# next(), 捕获StopIteration异常
with open('./7_1.py') as f:
	try:
		while True:
			line = next(f)
			print(line, end='')
	except StopIteration:
		pass

# 异常是通知我们迭代结束的。或者:
with open('./7_1.py') as f:
	while True:
		line = next(f, None)
		if line is None:
			break
		print(line, end='')

# for 语句来访问可迭代对象中的元素
items = [1, 2, 3]    # Invokes items.__iter__()
# Get the iterator
it = iter(items)     # Invokes it.__next__()
# Run the iterator
next(it)
