#. 访问定义在闭包内的变量 p242

# 闭包内层定义的变量对于外界来说完全是隔离

# 可以通过编写存取函数（accessor function,即getter/setter方法）并将它们作为函数属性附加到闭包上来提供对内层变量的访问支持。
def sample():
	n = 0
	# closure function
	def func():
		print('n=', n)

	# Accessor methods for n

	def get_n():
		return n

	def set_n(value):
		nonlocal n  # nonlocal声明使得编写函数来修改内层变量成为可能。
		n = value

	# Attach as function attributes
	func.get_n = get_n   # 函数属性能够将存取函数以直接的方式附加到闭包函数上，（工作起来像实例的方法）
	func.set_n = set_n
	return func

f = sample()
f()
f.set_n(10)
f()
f.get_n
