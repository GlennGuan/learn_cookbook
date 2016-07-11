#. 添加目录到sys.path

# 1 通过PYTHONPATH环境变量来添加
bash % env PYTHONPATH=/some/dir:/other/dir python3

>>>import sys
>>>sys.path

# 2 创建一个.pth文件，

myapplication.pth
/some/dir
/other/dir

.pth文件需要放在python的其中一个site-packages目录中。（管理员权限可以让.pth添加到整个系统级的python解释器上。）

# 或者手动调整
import sys   # 将目录名称硬编码到了源码中，这种做法极度脆弱，应竟可能避免。
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

# 更好的办法是做路径配置

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(dirname('__file__'), 'src'))

上面的代码将src目录添加到了sys.path中，而且src目录和执行插入操作的代码所在的目录是相同的
目录site-packages是第三方模块和包安装的位置。

用来配置路径的.pth文件必须出现在site-packages中，其中记录的路径可以指向系统中任何希望的目录
可以选择让代码保存在一个完全不同的目录中，只要这些目录都包含在.pth文件中即可。
