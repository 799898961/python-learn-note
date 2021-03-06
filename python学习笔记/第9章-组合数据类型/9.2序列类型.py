# 9.2序列类型.py

ls = ["python", 123, ".io"]
s = "python123"
print(ls[::-1], s[::-1])

# 序列类型：
# 具有先后关系的一组元素，元素之间可以相同，元素类型可以不同
# 它类似于数学元素序列：s0,s1,s2,……,sn

# 序列是一个基类类型
# 其衍生类型有：
# 字符串类型
# 元组类型
# 列表类型

# 6个操作符
# in 和 not in
# s + t 连接两个序列
# s*n 或 n*s 复制序列n次
# s[i] 索引
# 切片

# 函数：
# len(s)
# max(s) 和 min(s) 字符串按照字母序比较
# s.index(x,i,j) 返回序列从i开始到j位置中第一次出现元素x的位置
# s.count(x) 返回序列s中x出现的总次数

# 应用场景：
# 数据表示：
# 元组用于元素不改变的应用场景，更多用于固定搭配场景
# 列表更加灵活，他是最常用的序列类型
# 最主要作用：表示一组有序数据，进而操作他们

# 数据保护：
# 如果不希望数据被程序所修改，转换成元组类型
