# 定义带有额外状态的生成器函数 p123.
# 让生成器将状态暴露给用户

from collections import deque

class linehistory:
	def __init__(self, lines, histlen=3):
		self.lines = lines
		self.history = deque(maxlen=histlen)

	def __iter__(self):
		for lineno, line in enumerate(self.lines,1):
			self.history.append((lineno,line))
			yield line

	def clear(self):
		self.history.clear() 

# 会创建一个类实例，可以访问内部属性，比如history属性或者clear()方法
with open('/Users/sylvialin/Desktop/s_text.txt') as f:
	lines = linehistory(f)
	it = iter(lines)
	for line in lines:
		if 'python' in line:
			for lineno, hline in lines.history:
				print('{}:{}'.format(lineno, hline), end="")

				# 未完
