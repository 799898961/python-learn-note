# 10.5自动轨迹绘制.py

import turtle as t
t.title("自动颜色绘制")
t.setup(800,600,0,0)
t.color("red")
t.pensize(5)

# 数据读取模块
datals = []
fp = open("data.txt")
for line in fp :
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
fp.close()

# 自动绘制模块
for i in range(len(datals)) :
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1] :
        t.right(datals[i][2])
    else :
        t.left(datals[i][2])




# 基本思路
# (1) 定义数据文件格式 (接口)
# (2) 编写程序，根据文件接口解析参数绘制图形
# (3) 编制数据文件

# 数据接口定义：
# 每一个行 为一个操作
# 如：
# 300,1,144,0,1,0
# 第一个数据：前进距离
# 二：转向判断：0 —— 左转；1 —— 右转
# 三：转向角度
# 后三个：RGB颜色通道值 0~1之间的浮点数

# str.replace()函数
# 语法：str.replace(old, new[, max])
# 参数：
# old —— 将被替换的子字符串
# new —— 新字符串，用于替换old子字符串
# max —— 可选字符串, 替换不超过 max 次

# map()函数：
# 用法：第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
# 语法：map(function, iterable, ...)
# function —— 函数 可以是lambda函数，也可以是自定义函数
# iterable —— 一个或多个序列，可迭代对象

# 自动化思维：数据和功能分离，数据驱动的自动进行
# 接口化设计：格式化设计接口，清晰明了
# 二维数据应用：应用维度组织数据，二维数据最常用