# 12.5os库之路径操作.py

import os.path
import os

s = os.path.normpath("C://Users//79989//Documents//vscode-Python//第11章-数据的组织与处理//11.5关于实施乡村振兴战略的意见.txt")
fp = open(s, "r", encoding="utf-8")
print(os.path.getctime("C://Users//79989//Documents//vscode-Python//第11章-数据的组织与处理\\11.5关于实施乡村振兴战略的意见.txt"))



# os.path.normpath(path)

# 路径操作函数：
# (1) os.path.abspath(path)
# 返回path在当前系统中的绝对路径
# 例：
# os.path.abspath("12.5os库之路径操作.py")
# ——> C:\Users\79989\Documents\vscode-Python\第12章-程序设计方法学\12.5os库之路径操作.py
# 此时路径信息只是引号中的文件名加上源代码所在的文件夹所产生的路径
# 并无搜索功能
# 
# (2) os.path.normpath(path)
# 归一化path的表示形式，统一用\\分隔路径
# 例：
# os.path.normpath("C://Users//79989//Documents//vscode-Python
# ——> C:\\Users\\79989\\Documents\\vscode-Python
# 注意：
# 用print函数输出时可能显示单斜杠，但作为参数内部会用双斜杆
# 
# (3) os.path.relpath(path)
# 返回当前程序与文件之间的相对路径，即某文件夹下的某文件
# 例：
# os.path.relpath("C://Users//79989//Documents//vscode-Python//第11章-数据的组织与处理//11.5关于实施乡村振兴战略的意见.txt")
# ——> ..\第11章-数据的组织与处理\11.5关于实施乡村振兴战略的意见.txt
# 
# (4) os.path.dirname(path)
# 返回path中的目录名称
# 例：os.path.dirname("C://Users//79989//Documents//vscode-Python//第11章-数据的组织与处理//11.5关于实施乡村振兴战略的意见.txt")
# ——> C://Users//79989//Documents//vscode-Python//第11章-数据的组织与处理
#
# (5) os.path.basename(path)
# 返回path中最后的文件名称
# 例：
# os.path.basename("C://Users//79989//Documents//vscode-Python//第11章-数据的组织与处理//11.5关于实施乡村振兴战略的意见.txt")
# ——> 11.5关于实施乡村振兴战略的意见.txt
# 
# (6) os.path.join(path1[, path2[, ...]]) 
# 将path1与path2，path3……进行组合，返回一个路径字符串
# 例：
# os.path.join("D:/", "pye/file.txt")
# ——> D:/pye/file.txt
#
# (7) os.path.exists(path)
# 判断path对应文件或目录是否存在，存在true，不存在或文件损坏false
# 例：
# os.path.exists("D://pye//file.txt")
# false
# 
# (8) os.path.exists(path)
# 判断path对应文件或目录是否存在，存在或文件损坏true，不存在false
# 
# (9) os.path.isfile(path)
# 判断对应的路径是否为已存在的文件，返回true或false
# 例：
# os.path.isfile("D://pye//file.txt")
# 假设该文件存在 ——> Ture
#
# (10) os.path.isdir(path)
# 判断对应路径是否为已存在的目录
# 例：
# os.path.isdir("D://pye//file.txt")
# 假设该文件存在 ——> False
# 因为该路径所指向的为一个文件，若为目录应为
# os.path.isdir("D://pye")
# 假设该文件存在 ——> Ture
#
# (11) os.path.getatime(path) 
# 返回path对应文件或目录上一次的访问时间(浮点型时间)
#
# (12) os.path.getmtime(path)
# 返回path对应文件或目录最近一次的修改时间(浮点型时间)
#
# (13) os.path.getctime(path)
# 返回path对应文件或目录的创建时间(浮点型时间)
#
# (14) os.path.getsize(path)
# 返回path对应文件大小，以字节为单位，如果文件不存在就返回错误