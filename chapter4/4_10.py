#. 以索引-值对的形式迭代序列

# 迭代一个序列，记下当前处理到的元素索引

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):  # 索引从1开始的话 enumerate(my_list, 1)
	print(idx, val)

# 跟踪记录文件中的行号

def parse_date(filename):
	with open(filename, 'rt') as f:
		for lineno, line in enumerate(f, 1):
			fields = line.split()
