# 6.1遍历循环.py

# 字符串遍历：
for c in "python123":
    print(c, end=",")
print()
# 列表遍历：
for item in [123, "python", 456]:
    print(item, end=",")
print() 



# 遍历某个结构形成的循环运行方式
# for <循环变量> in <遍历结构>:
#       <语句块>
# 每次循环，能从遍历结构中逐一提取元素，放在循环变量里
# 并执行一次语句块

# 计数循环n次
# for i in range(n):
#       <语句块>
# 遍历由range()函数产生的数字序列，产生循环

# 计数循环 特定次
# for i in range(m,n,k):
#       <语句块>
# m —— 起始数字  n —— 终止数字  k —— 步长
# 循环次数：(n-m)次

# 字符串遍历循环
# for c in s：
#       <语句块>

# 列表遍历循环
# for item in ls:
#       <语句块>
# ls是一个列表，遍历其每一个元素，产生循环

# 文件遍历循环
# for line in fi:
#       <语句块>
# fi是一个文件标识符，遍历其每行，产生循环