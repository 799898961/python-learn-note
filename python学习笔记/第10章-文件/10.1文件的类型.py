# 10.1文件的类型.py

tf = open("c:\\Users\\79989\\Documents\\vscode-Python\\第10章-文件\\text.txt", "rt", encoding="UTF-8")
bf = open("c:\\Users\\79989\\Documents\\vscode-Python\\第10章-文件\\text.txt", "rb")
print(tf.readline())
print(bf.readline())  
tf.close()
bf.close()



# 文件是数据的抽象和集合
# 文件是存储在辅助储存器上的数据序列
# 文件是数据储存的一种形式

# 文件的展现形态：
# 文本文件
# 二进制文件
# 本质上，所有文件都是二进制形式储存
# 形式上，所有文件采用两种方式展示

# 文本文件：
# 由单一特定编码组成的文件，如UTF-8
# 由于存在编码，也被看成是存储着的长字符串
# 适用于例如：txt文件、py文件

# 二进制文件：
# 直接由比特0和1组成，没有统一的字符编码
# 一般存在二进制0和1的组织结构，即文件格式
# 如：jpg文件 mp3文件

