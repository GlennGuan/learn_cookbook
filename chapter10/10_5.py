#.  让各个目录下的代码在统一的命名空间下导入

foo-package/
	spam/  # spam为公共的命名空间
		blah.py

bar-package/
	spam/
		grok.py   # 要忽略目录中的__init__.py文件

import sys
sys.path.extend(['foo-package','bar-package'])
import spam.blah
import spam.grok

这里的工作原理：命名空间包（namespace package)
用来合并不同目录下的代码，把他们放在统一的命名空间之下进行管理
确保在统一命名空间的顶层目录中不包含__init__.py文件。

import spam  
spam.__path__
_NamespacePath(['foo-package/spam','bar-package/spam']) 解释器创建一个列表，把所有恰好包含有这个包名的目录都囊括在内。

# 把自己的代码目录和其他的包一起添加到sys.path中，就可以同其他的spam包合并在一起

#spam.__file__ 缺少这个属性，这个包就是命名空间。

PEP 420 http://www.python.org/dev/peps/pep-0420
