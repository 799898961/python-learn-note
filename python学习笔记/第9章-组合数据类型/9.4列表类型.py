# 9.4列表类型.py

ls = ["cat", "dog", "tiger", 1024]
lt = [100, 120, 123]
lis = ["a".split(",") for c in ls]
ls[0:2] = lt
print(lis)
a = [0,1,3,4,5,0]
print(a.index(0))
sorted(lt)

# 列表是序列类型的扩展，创建后可以随意被修改
# 使用方括号[] 或 list() 创建， 元素间用逗号分隔
# 列表中各元素类型可以不同，无长度限制

# 仅用等号=来传递值并未真正形成一个列表，而是将同一个列表赋予了不同的名字
# 不同的名字都指向同一个列表
# 若使用方括号或list()，那么就真正的创建了一个列表（内存层面的）
# 只是使用等号对变量赋值，只是给列表赋予了新的名字（指针层面的）

# 列表类型的操作函数和方法 
# (1) ls[i] = x  替换列表ls第i元素为x
# (2) ls[i:j:k] = lt  用列表lt替换ls切片后所对应元素子列表
#     即：先对ls进行切片，再对切片部分用lt进行替换
# (3) del ls[i]  删除列表ls的第i个元素
# (4) del ls[i:j:k]  切片删除
# (5) ls += lt  更新列表ls，将列表lt的元素增加到列表ls中
# (6) ls *= n  更新列表ls，其元素重复n次
# 
# (7) ls.reverse()  将列表ls中的元素反转
# (8) ls.insert(i,x)  在列表ls的第i位置增加元素x 即：增加的元素x为第i号位
# (9) ls.append(x)  在列表ls最后增加一个元素x
# (10) ls.clear() 清除ls中所有元素 
# (11) ls.pop(i) 从ls中取出(返回)第i位置上的元素并在ls中删除该元素
# (12) ls.copy() 生成一个新列表，赋值ls中所有元素
# (13) ls.remove(x) 将列表ls中出现的第一个元素x删除
# (14) ls.index(x[,i,j]) 返回序列 [从i开始到j位置中] 第一次出现元素x的位置
# (15) ls.sort()  对已经存在的列表进行操作，无返回值
# 原型：list.sort(fun, key=None, reverse=Flase)
# fun：表明此sort函数是基于何种算法进行排序的，一般情况下不会重写此参数，可忽略
# key：用来指定一个函数，此函数在每次元素比较时被调用，此函数代表排序的规则，
#      也就是你按照什么规则对你的序列进行排序；一般用lambda函数指定。
# reverse：指定排序规则，reverse=True（升序），reverse=Flase（降序），默认降序。


# sorted()函数
# 使用：sorted(list)
# 表示：对所有的可迭代对象进行排序操作，返回的是一个新的列表，不是在原来的基础上进行操作。
# 原型：sorted(iterable, key=None, reverse=Flase)
# iterable：可迭代对象 

