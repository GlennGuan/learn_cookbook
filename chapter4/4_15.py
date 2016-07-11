# 合并多个有序序列，再对整个有序序列进行迭代

#  操作对象有序序列

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
	print(c)

# heapq.merge的迭代性质意味着它对所有提供的序列都不会做一次性读取。
# 可以利用它处理非常长的序列，开销却非常小。

with open('./4_1.py', 'r') as file1,open('./4_2.py','r') as file2,open('./merged.py','wt') as outf:
	for line in heapq.merge(file1, file2):
		outf.write(line)

# heapq.merge()要求所有的输入序列都是有序的