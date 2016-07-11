# 用生成器创建新的迭代模式 p117.

# 实现一个自定义的迭代模式，区别于常见的内建函数（range(),reversed())

# 可使用生成器函数来定义

def frange(start, stop, increment):
	x = start
	while x < stop:
		yield x   # 函数中出现了yield语句就会将其转变成生成器。（生成器只会在响应迭代操作时才运作。
		x += increment

for n in frange(0, 4, 0.5):
	print(n, end='')

print(list(frange(0, 1, 0.125)))

# 了解这样的函数底层运作机制

def countdown(n):
	print('Strating to count from', n)
	while n > 0:
		yield n
		n -= 1
	print('Done!')

# create the generator notice on output appears
c = countdown(3)
print(c)

# run to first yield and emit a value
next(c)

# run to next yield
next(c)

# run to next yield (iteration stops)
next(c)
# 生成器的核心特性只会响应迭代过程中的‘next'操作才会运行。一旦生成器函数返回，迭代也就停止了。
# for 

