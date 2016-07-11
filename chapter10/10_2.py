#. 对所有符号的导入进行精确控制

# 当用户使用from module import *语句时，我们希望对从模块或包中导入的符号进行精确控制。

# 在模块中定义一个变量__all__,用来显式列出可导出的符号名
# somemodule.py

def spam():
	pass

def grok():
	pass

blah = 42

# only export 'spam' and 'grok'
__all__ = ['spam', 'grok']

# 如果定义了__all__中包含有未定义的名称，那么执行import语句时会产生一个AttributeError异常
# 如果定义了__all__，那么只有显示李处的符号才会被导出。
