# 11.3二维数据note.py

# 逐一遍历二维数据
ls = [[1,2],[3,4],[5,6]]
for row in ls :
    for column in row :
        print(column,end=" ")


# 一：二维数据的表示
# 列表表示 
# 使用双层for循环遍历每个元素

# 二：二维数据的存储
# CSV数据存储格式
# Comma-Separated Values 用逗号分隔值
# 用逗号分隔值的一种方式
# 国际通用的一二维数据存储格式，一般 .csv 扩展名
# 每行一个一维数据，采用逗号分隔，无空行
# 规定：
# (1)如果某个元素缺失，逗号仍要保留
# (2)二维数据的表头可以作为数据存储，也可以另行存储
# (3)逗号为英文半角逗号，逗号与数据之间无额外空格

# 按行存或按列存都可以
# 一般索引习惯：ls[row][column]，先行后列
# 根据一般习惯，外层每个元素是一行，按行存

# 三.二维数据的处理
# 从csv格式文件中读入数据
# fo = open(fname)
# ls = []
# for line in fo :
#     line = line.replace("\n", "")
#     ls.append(line.split(","))
# fo.close()

# 将数据写入csv格式的文件
# ls = [[],[],[]]
# f = open(fname, "w")
# for item in ls :
#     f.write(",".join(item) + "\n")
# f.close()


# 