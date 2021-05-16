# 3.5daydayupQ4.py
def Dayup(df):
# def用于自定义函数，圆括号内为传入参数
    dayup = 1
    for i in range (365):
        if i%7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup

dayfactor = 0.01
while (Dayup(dayfactor)<37.78):
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f}" .format(dayfactor))