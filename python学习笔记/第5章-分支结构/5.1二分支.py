# 5.1二分支.py
guess = eval(input())
print("猜{}了" .format("对" if guess==99 else "错"))
str = "对" if guess==99 else "错"
print(str)
# 简单表达二分支的紧凑形式

# if True:
#    语句块1
# else:
#    语句块2
# 上述语句中，else的语句不会被执行