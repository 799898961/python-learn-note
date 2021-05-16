#tempconcvert.py
tempstr = input("请输入带有符号的温度值：")
if tempstr[-1] in ['F','f']:
    C = (eval(tempstr[0:-1]) - 32)/1.8
    print("转换后的温度为{:.2f}C" .format(C))
elif tempstr[-1] in ['C','c']:
    F = 1.8*eval(tempstr[0:-1]) + 32
    print("转换后的温度为{:.2f}F" .format(F))
else:
    print("格式输入错误！")

# input() 函数接受一个标准输入数据，返回为 string (字符型) 类型 
# 在小括号内的加双引号的中间可加入提示词
# 例： 变量 = input("提示词")

# print()
# format()格式化函数
# 基本语法是通过 {} 和 : 来代替以前的 % 。

# 列表类型：与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
# 第一个索引为 0 ，第二个索引是1，依此类推。
# 可以进行的操作包括索引，切片，加，乘，检查成员。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
# 如下所示：
# list1 = ['Google', 'Runoob', 1997, 2000] 
# list2 = [1, 2, 3, 4, 5 ] 
# list3 = ["a", "b", "c", "d"]
# 使用下标索引来访问列表中的值，同样也可以使用方括号的形式截取字符

# in 字典操作符 用于判断字符串是否在列表中
# 相反 not in 判断是否不在列表当中
# 例：
# dict = {'name':'wzh', 'age':7}
# if 'age' in dict:
# if 'sex' in dict:
# if 'age' not in dict:

# eval()函数 (evaluate  v.评估，估计)
# eval() 函数用来执行一个字符串表达式，
# 并返回表达式的值。
# 即：去掉字符串类型最外面的引号，并执行余下语句，保留字符的原本属性
# 例：eval("1+2") 结果为 3 (整数型)
#     eval('"1+2"') 结果为 1+2 (字符串型)
# 也可以直接用来提取用户输入的多个值
# 例：
# a,b=eval(input()) 输入 1,2 得到 a=1，b=2

# 字符串的索引：
# 字符串是字符的有序集合，可以通过其位置来获得具体的元素。
# 在 python 中，字符串中的字符是通过索引来提取的，索引从 0 开始。
# 在[x:y]中可以取负值，表示从末尾提取，最后一个为 -1，倒数第二个为 -2，
# 即程序认为可以从结束处反向计数。
# 正向递增序号：[0:x]
# 反向递减序号：[n:-1]
# 第一个元素的号码为 0 可理解为 偏移
# 即：字符串中第一个元素的偏移为 0 
# 字符串中最后一个元素的偏移为-1
# 分片提取：
# 如果没有指定值，则分片的边界默认为0和序列的长度
# 以 string 字符串为例
# (1)str[1:3]获取从偏移为1的字符一直到偏移为3的字符串，不包括偏移为3的字符串 : "tr"
# (2)str[1:] 获取从偏移为1的字符一直到字符串的最后一个字符（包括最后一个字符）: "tring"
# (3)str[:3] 获取从偏移为0的字符一直到偏移为3的字符串，不包括偏移为3的字符串 : "str"
# (4)str[:-1] 获取从偏移为0的字符一直到最后一个字符（不包括最后一个字符串）: "strin"
# (5)str[:] 获取字符串从开始到结尾的所有元素 : "string"
# (6)str[-3:-1] 获取偏移为 -3 到偏移为 -1 的字符，不包括偏移为 -1 的字符 : "in"
# (7)str[-1:-3] 和 str[2:0] 获取的为空字符，系统不提示错误: ""