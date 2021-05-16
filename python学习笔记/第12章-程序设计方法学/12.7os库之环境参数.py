# 12.7os库之环境参数.py

import os

path = os.getcwd()
os.chdir(path)
print(path)
print(os.getlogin())
print(os.urandom(10))

# os.chdir(path)
# 修改当前程序操作的路径，修改将当前程序的执行路径
#
# os.getcwd()
# 返回程序的当前路径
# 
# os.getlogin()
# 返回当前系统登录用户名称
#
# os.urandom(n)
# 获得n个字节长度的随机字符串，通常用于加解密运算
#
# 