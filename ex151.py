# -*- coding: utf-8 -*-
# 从系统导入参数
from sys import argv
# 选取两个参数，script, filename
script, filename = argv
# 给txt变量赋值，即打开文件
txt = open (filename)
# 打印这句话
print ("Here's your file %r: " % filename)
# 打印打开的文档内容
print (txt.read ())
# 继续打一个文件名
print ("Type the filename again: ")
# 这次文件输入为键盘输入
file_again = raw_input (">")
# 再次打开文件
txt_again = open (file_again)
# 打印打开文件的内容
print (txt_again.read())