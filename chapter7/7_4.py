#. 从函数中返回多个值

# 解决方案
# 简单返回一个元祖
def myfun():
	return 1, 2, 3

print(myfun())  # (1, 2, 3)

a, b, c = myfun() # 简单的元组解包（1.1节）
print(a, b, c)

x = (1, 2)  # with parentheses
y = 1, 2    # without parentheses
