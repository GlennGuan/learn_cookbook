#.  让带有N个参数的可调用对象以较少的参数形式调用 p232

def spam(a, b, c, d):
	print(a, b, c, d)

from functools import partial     # 函数partial() 给一个或多个参数指定固定的值。 对特定参数赋了固定值并返回了一个全新的可调用对象。
s1 = partial(spam,1)  # a = 1
s1(2, 3, 4)
s1(4, 5, 6)

s2 = partial(spam, c=23,d=42)  # 如果指定C 没有指定D s2函数就出错。
s2(1, 2)
s2(2, 3)

s3 = partial(spam, 1, 2, d=42)

s3(2)
s3(9)
s3(11)


# 可以用下面的函数来计算两点之间的距离
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

import math
def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return math.hypot(x2 - x1, y2 - y1)

# 假设想根据这些点之间的距离来对它们排序。 列表sort（）方法可接受一个Key参数，它可用来做自定义的排序处理。（只能接受单参数的函数）

pt = (4, 3)

points.sort(key=partial(distance,pt))
print(points)

# 未完。。。。
