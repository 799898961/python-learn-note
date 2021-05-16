# 5.2多分支——对不同分数的分级问题
score = eval(input("请输入成绩: "))
if score >= 60 and score < 70:
    grade = "D"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 90 and score < 100:
    grade = "A"
print("输入的成绩属于{}级别" .format(grade))


# 逻辑运算符
# and   逻辑与  x and y
# or    逻辑或  x or y
# not   逻辑非  not x

# if not True:
#    语句块1
# else:
#    语句块2
# 不会执行语句块1