#. 在回调函数中携带额外的状态  p239

# 回调函数可以携带额外的状态以便在回调函数内部使用。

# 调用一个回调函数
def apply_async(func, args, *, callback):   # 线程，进程 定时器。
	# compute the result
	result = func(*args)

	# invoke the callback with the result
	callback(result)

def print_result(result):
	print('Go:', result)

def add(x, y):
	return x + y

apply_async(add, (2, 3), callback=print_result)

apply_async(add, ("hello", "world"), callback=print_result)  # 这里并没有传入其他的信息到函数。

# 回调函数可以同其他变量或者部分环境进行交互时，缺乏这类信息就会带来问题。

# 在回调函数中携带额外信息的方法是使用绑定方法而不是普通的函数

# 保存了一个内部的序列号码，每当接收到一个结果是递增这个号码

class ResultHandler:
	def __init__(self):
		self.sequence = 0
	def handler(self, result):
		self.sequence += 1
		print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler() # 创建一个实例并将绑定方法handler当做回调函数来用

apply_async(add, (2, 3), callback=r.handler)

apply_async(add, ("hello", "world"), callback=r.handler)

# 作为类的替代方案，也可以使用闭包来捕获状态
def make_handler():
	sequence = 0
	def handler(result):
		nonlocal sequence
		sequence += 1
		print('[{}] Got: {}'.format(sequence, result))
	return handler

handler = make_handler()

apply_async(add, (2, 3), callback=handler)

apply_async(add, ("hello", "world"), callback=handler)


# 利用携程来完成同样的任务：
def make_handler():
	sequence = 0
	while True:
		result = yield
		sequence += 1
		print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler)  # advance to the yield


apply_async(add, (2, 3), callback=handler.send)

apply_async(add, ("hello", "world"), callback=handler.send)

# 最后同样重要，通过额外的参数在回调函数中携带状态，然后用parital()来处理参数个数的问题（7.8）

class SequenceNo:
	def __init__(self):
		self.sequence = 0

def handler(result, seq):
	seq.sequence += 1
	print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial

apply_async(add, (2, 3), callback=partial(handler, seq=seq))

apply_async(add, ("hello", "world"), callback=partial(handler, seq=seq))

# 详细注解见p239
apply_async(add, (2, 3), callback=lambda r: handler(r, seq))

apply_async(add, ("hello", "world"), callback=lambda r: handler(r, seq))
