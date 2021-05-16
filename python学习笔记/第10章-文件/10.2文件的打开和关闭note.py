# 10.2文件的打开和关闭note.py



# 文件处理步骤：打开——操作——关闭

# 读文件：
# a.read(size)
# a.readline(size)
# a.readlines(hint)

# 写文件：
# a.write(s)
# a.writelines(lines)
# a.seek(offset)

# 文件的打开
# <变量名> = open(<文件名>, <打开模式>)

# 文件打开模式：
# r     只读模式，默认值，若文件不存在，返回FileNotFoundError
# w     覆盖写模式，文件不存在则创建，存在则完全覆盖
# x     创建写模式，文件不存在则创建，存在则报错
# a     追加写模式，文件不存在则创建，存在则在文件最后追加内容
# b     二进制文件模式
# t     文本文件模式，默认值
# +     与r、w、x、a一同使用，在原功能基础上增加同时读写功能
