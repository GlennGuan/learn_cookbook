##7.1 编写可接受任意数量参数的函数.

###  解决方案

# 接受任意数量的位置参数 *
def avg(first, *rest):   # rest是一个元组，将视为序列处理。
	return (first + sum(rest)) / (1 + len(rest))

print(avg(1,2))
print(avg(1,2,3,4))

# 接受任意数量的关键字参数  **
import html

def make_element(name, value, **attrs):   # attrs是字典
	keyvals = {' %s="%s"' % item for item in attrs.items()}
	attr_str = ''.join(keyvals) # 连接参数
	#print(attr_str)  # quantity="6" size="large"
	element = '<{name}{attrs}>{value}</{name}>'.format(   # format格式化函数
		         name = name,
		         #attrs = attrs,  #{'size': 'large', 'quantity': 6}
		         attrs = attr_str,
		         value = value)#html.escape(value))
	return element

print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))

# 同时接受任意数量的位置参数和关键字参数
def anyargs(*args, **kwargs):
	print(args)   # A tuple
	print(kwargs)  # A dict

# 讨论  详解见7.2
def a(x, *args, y):
	pass


def b(x, *args, y, **kwargs):
	pass

