#. 用函数替代只有单个方法的类 p236

# 有一个只定义了一个方法的类（除__init__()方法外）。
# 解决：通过闭包将其转换成函数。
# 这个允许用户通过某种模板方案来获取URL

from urllib.request import urlopen

class UrlTemplate:
	def __init__(self, template):   # 保存template的值。
		self.template = template
	def open(self, **kwargs):
		return urlopen(self.template.format_map(kwargs))

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')   # download stock data from yahoo
for line in yahoo.open(names='IBM,AAPL,FB', fields='sllclv'):
	print(line.decode('utf-8'))

# 以上类可以用一个简单的韩式来取代
def urltemplate(template):
	def opener(**kwargs):
		return urlopen(template.format_map(kwargs))
	return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}') 
for line in yahoo(names='IBM,AAPL,FB', fields='sllclv'):
	print(line.decode('utf-8'))

# 闭包就是一个函数，但是它还保存着额外的变量环境，使得这些变量可以在函数中使用。
# 闭包的核心特性就是它可以记住定义闭包时的环境。
# opener()函数可以记住参数template的值，然后在随后的调用中使用。
