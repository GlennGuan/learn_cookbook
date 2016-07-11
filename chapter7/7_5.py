#. 定义带有默认参数的函数 p226

# 一个或多个参数是可选的并且带有默认值

def spam(a, b=42):
	print(a, b)

spam(1)      # 1 42
spam(1, 2)	 # 1 2

# Using a list as a default value
def spam(a, b=None):   # 不建议参数默认值为可变容器
	if b is None:
		b = []


# 编写代码来检测可选参数是否被赋予了某个特定的值
_no_value = object()

def spam(a, b = _no_value):   # 不传递参数和传递None之间的区别。
	if b is _no_value:
		print('No b value supplied')
	else:
		print(a, b)

spam(1)
spam(1,2)
spam(1,None)

# 介绍不建议参数默认值为可变容器
x = 42
def spam(a, b=x):  # 修改x的值并没有对函数产生任何效果，在定义函数的时候已经确定好值了。
	print(a, b)

spam(1)
x = 23
spam(1)

def spam(a, b=[]):  # NO!  默认值在函数体之外被修改。
    print(b)
    return(b)
y = spam(1)
print(y)
y.append(99)
y.append('Yow!')
print(y)
spam(1)
