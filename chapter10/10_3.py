#. 用相对名称来导入包中的子模块

相对导入只在特定的条件下才起作用
模块必须位于一个合适的包中才可以
位于脚本顶层目录的模块不能使用相对导入。
如果包的某个部分是直接以脚本的形式执行。

% python3 mypackage/A/spam.py  # Relative imports fail

% python3 -m mypackage.A.spam  # Relative imports work

mypackage/
	__init__.py
	A/
		__init__.py
		spam.py
		grok.py
	B/
		__init__.py
		bar.py
# mypackage/A/spam.py

from . import grok  # 在同一个目录导入grok

from ..B import bar # 导入不同目录中的模块B.bar(仅路径在mypackage下有效)

以上是相对spam.py文件的位置来进行操作的

from mypackage.A import grok  # OK
from . import grok  # ok
import grok # Error (not found)   使用绝对名称的缺点在于这么做会将最顶层的包名称硬编码到源代码中，这使得代码更加脆弱。

.意味着在当前目录中查找
..B表示在../B目录中查找

PEP 328 http://www.python.org/dev/peps/pep-0328
