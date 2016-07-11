#. 对迭代器做切片操作
# 普通的切片操作符在这里不管用

# itertools.islice()  对迭代器和生成器做切片操作

def count(n):
	while True:
		yield n
		n += 1
c = count(0)
#print(c[10:20])  # 'generator' object is not subscriptable

# Now using islice()
import itertools
for x in itertools.islice(c, 10, 20):
	print(x)

# 不知道可迭代对象的长度
# islice()产生的结果是一个迭代器，产生出所需要的切片元素。
# 这是要通过访问并丢弃所有起始索引之前的元素来实现的
# 之后还要访问前面的数据，那就应该先将数据转到列表中。
