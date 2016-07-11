# 重新加载模块

# spam.py

def bar():
	print('bar')

def grok():
	print('grok')

交互式模式
>>>import spam
>>>from spam import grok # 对于from module import name这样的语句，reload()是不会去更新的。
>>>spam.bar()
bar
>>>grok()
grok
>>>

# 改写
def grok():
	print('New grok')

>>>import imp
>>>imp.reload(spam)   # reload()会擦除模块底层字典（__dict__)的内容，并通过重新执行模块的源代码来刷新它
<module 'spam' from './spam.py'>
>>>spam.bar()
bar
>>>grok()
grok
>>>spam.grok() # 重载并不会是我们预期的结果。
New grok
>>>
