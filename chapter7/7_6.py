#. 定义匿名或内联函数
# 想法的初衷 提供一个短小的回调函数为sort()这样的操作作用，但是又不想通过def语句编写一个单行的函数。

add = lambda x, y: x + y

# 等价于
def add(x, y):
	return x + y

# lambda表达式可用在如下的上下文环境中，比如排序或者对数据进行整理时：
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']

print(sorted(names, key=lambda name: name.split()[-1].lower()))   # lambda ['beazley','jones','hettinger','batchelder']

