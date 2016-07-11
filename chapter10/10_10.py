#. 使用字符串中给定的名称导入模块 p420

# 当模块或包的名称以字符串的形式给出时，
>>>import importlib
>>>math = importlib.import_module('math')
>>>math.sin(2)

>>>mod = importlib.import_module('urllib.request')
>>>u = mod.urlopen('http://www.python.org')

# Same as 'from' . import b'
b = importlib.import_module('b', __package__)
