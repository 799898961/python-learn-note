# 9.6字典类型.py

'''
d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
a = "伦敦" 
lis = list(d)
print(lis)
for ch in lis :
    print("{:<}: {:<5}" .format(ch, d[ch]), end="    ")
'''


all_class = []
single_class = {"class_name": "202", "students": []}
student = {
    "name" : "wzh",
    "student_id" : "193407020229",
    "sex" : "男"
}

student["math_score"] = 100


single_class["students"].append(student)
all_class.append(single_class)
print(all_class[0]["students"][0]["math_score"])

# print(d.get("yi", 123))
# print(list(d))
# 直接类型转换是将键转换为列表
# print(list(d.items()))
# 键值对转换是将键值对做成元组类型，然后返回列表

# 理解映射：
# 映射是一种键(索引)和值(数据)的对应

# 序列类型由0……n整数作为数据的索引
# 映射类型由用户为数据自定义索引

# 字典类型是“映射”的体现
# 键值对：键是对数据索引的扩展
# 字典是键值对的集合，键值对之间无序

# 生成字典类型：
# 大括号{} 或 dict() 创建，键值对用冒号:表示
# 如：
# {<键1>:<值1>, <键2>:<值2>,……,<键n>:<值n>}

# 在字典变量中，通过键获得值
# <字典变量> = {<键1>:<值1>, <键2>:<值2>,……,<键n>:<值n>}
# 也可以通过字典变量，赋予新的键和值的关系
# <值> = <字典变量>[<键>]   ! 存疑 !
# <字典变量>[<键>] = <值>
# [] 用来向字典变量中索引或增加元素

# type(x) 返回变量x的类型

# 处理函数或方法：
# (1) del d[k]    删除字典d中键k对应的数据值
# (2) k in d      判断键k是否在字典d中 true/false
# (3) d.keys()    返回字典d中所有键的信息
# (4) d.values()  返回字典d中所有值的信息
# (5) d.item()    返回字典d中所有键值对的信息  
# (6) d.get(k,<default>)    键k存在，则返回相应值，不在则返回<default>值 自定义<default>内容，可以是变量，数值，字符串
# (7) d.pop(k,<default>)    键k存在，则取出相应值，不在则返回<default>值
# (8) d.popitem()           随机从字典d中取出一个键值对，以元组形式返回
# (9) d.clear()             删除所有的键值对
# (10) len(d)               返回字典d中元素(键值对)的个数
  
# keys 和 values 返回的是 字典的 keys 和 values 类型
# 可以用for...in 做遍历，但不能当做列表类型操作

# 映射的表达：
# 如：统计数据的出现次数，数据是键，次数是值
# 最主要作用：表达键值对数据进而操作它们