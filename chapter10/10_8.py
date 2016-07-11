#. 读取包中的数据文件

mypackage/
	__init__.py
	somedata.dat
	spam.py

# spam.py  读取somedata.dat中的内容
import pkgutil
data = pkgutil.geit_data(__package__, 'somedata.dat')

相对于内建的I/O函数
1）：绝对路径。 每个模块在__file__变量中保存了全路径。获取文件的位置很麻烦，I/O操作都必须使用文件名的绝对路径
2）：文件类型。 pkgutil.get_data()函数，无论以什么样的形式安装或安装到了哪里，都能够用它来获取数据。把工作内容以字节串的形式返回给我们。

get_data() 参数  包含有包名的字符串（或者__package__）  参数 获取文件相对于包的名称。（如果有必要可以使用标准unix路径名规则进入不同的目录，最后的目录仍然在包的内部）
