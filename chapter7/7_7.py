#.` 匿名函数中绑定变量的值 p230

# 在函数定义的时候完成对特定变量的绑定

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y  # lambda中的x是一个自由变量，在运行时才进行绑定而不是在定义的时候绑定。

print(a(10))
print(b(10))

# 在定义的时候绑定变量
x=11
c = lambda y, x=x: x + y
x=21
d = lambda y, x=x: x + y

print(c(10))
print(d(10))


#------------------------------------------------------------|
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
	print(f(0))

funcs = [lambda x,n=n: x+n for n in range(5)]
for f in funcs:
	print(f(0))
