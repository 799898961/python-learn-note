# 5.4calbmiV1.py
height = eval(input("请输入身高(单位：米)："))
weight = eval(input("请输入体重(单位：公斤)："))
bmi = weight / pow(height, 2)
print("您的bmi值为：{:.2f}" .format(bmi))
who = ''
nat = ''
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi <25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi <28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI指标为：国际\"{}\"，国内\"{}\"" .format(who, nat))


# 由于国际和国内的BMI指标不一样，所以利用指标间的空挡进行分类
# 可以达到程序的目的