# 3.7weeknameprint V1.py
weekstr1 = "星期一星期二星期三星期四星期五星期六星期日"
weekid1 = eval(input("请输入星期数字(1-7): "))
pos1 = (weekid1 - 1) * 3
print(weekstr1[pos1 : pos1+3])

#3.7weeknameprint V2.py
weekstr2 = "一二三四五六日"
weekid2 = eval(input("请输入星期数字(1-7): "))
print("星期" + weekstr2[weekid2-1])