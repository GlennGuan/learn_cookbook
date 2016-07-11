#. 编写只接受关键字参数的函数 page223

# 解决方案

def recv(maxsize, * , block):
	'Receives a message'
	pass

recv(1024, True) # TypeError
recv(1024, block=True) # ok

# 接受任意数量的位置参数的函数来指定关键字参数
def mininum(*values, clip = None):
	m = min(values)
	if clip is not None:
		m = clip if clip > m else m
	return m

print(mininum(1, 5, 2, -5, 10))      # returns -5
print(mininum(1, 5, 2, -5, clip=0))  # returns 0

# keyword-only参数(*参数之后出现的参数 **kwargs是其中之一)
# 提高代码可读性。
