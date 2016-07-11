#. 把模块按层次结构组织成包

# 创建一个软件包结构只要把代码按照所希望的方式在文件系统上进行组织，并确保每个目录中都定义了一个__init__.py文件

# graphics/
	# __init__.py   #__init__.py包含可选的初始化代码，遇到软件包中不同层次的模块时会出发运行。
	# primitive/
	# 	__init__.py
	# 	line.py
	# 	fill.py
	# 	text.py
	# formats/
	# 	__init__.py
	# 	png.py
	# 	jpg.py

# 以上结构完成我们可以执行import语句
# import graphics   # 文件graphics/__init__.py会被导入形成graphics命名空间中的内容。
# import graphics.formats.jpg # 文件graphics/__init__.py和graphics/formats/__init__.py都会在最终导入文件graphics/formats/jpg.py之前先导入。
# import graphics.primitive.line
# from graphics.primitive import line
# import graphics.formats.jpg as jpg

# 可以用__init__.py文件来自动加载子模块：
# graphics/formats/__init__.py
from . import jpg
from . import png

# 用户只需要使用一条单独的import graphics.formats语句就可以导入jpg和png模块了。
