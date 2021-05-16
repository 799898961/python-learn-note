# 6.4循环的高级应用.py
for c in "python":
    if c=='t':
        continue
    print(c, end="")
else:
    print("正常退出")

for c in "python":
    if c=='t':
        break
    print(c, end="")
else:
    print("正常退出")

# 方法：
# for循环：
# for <循环变量> in <遍历结构>:
#       <语句块1>
# else:
#       <语句块2>
# while循环：
# while <条件>:
#       <语句块1>
# else:
#       <语句块2>

# 当循环没有被break语句退出时，执行else语句块
# else语句块作为“正常”完成循环的一种奖励