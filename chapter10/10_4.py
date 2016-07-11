#. 将模块分解成多个文件p411

# mymodule.py

class A:
	def spam(self):
		print('A.spam')
class B(A):
	def bar(self):
		print('B.bar')

mymodule/
	__init__.py
	a.py
	b.py

# a.py
class A:
	def spam(self):
		print('A.spam')

# b.py
from .a import A  # class B把 class A当做基类来访问。
class B(A):
	def bar(self):
		print('B.bar')

# __init__.py   # 粘合，一次性将所有需要的组件都导进来了（如果模块非常庞大的话？)

from .a import A
from .b import B
		
# “惰性”导入概念
# __init__.py

def A():
	from .a import A
	return A()
def B():
	from .b import B
	return B()

# 惰性加载在真实世界中的应用，可以参考标准库中multiprocessing/__init__.py中的源代码。
