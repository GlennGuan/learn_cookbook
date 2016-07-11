# 让目录或zip文件成为可运行的脚本 p417

myapplication/
	spam.py
	bar.py
	grok.py
	__main__.py
bash % python3 myapplication
解释器会把__main__.py文件作为主程序执行。

# 把代码打包进一个zip文件中时同样有效

bash % ls
spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py
bash % python3 myapp.zip
...output from __main__.py...
