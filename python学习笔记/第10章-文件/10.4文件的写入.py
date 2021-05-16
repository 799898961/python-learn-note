# 10.4文件的写入.py

fo = open("test1.txt", "w+", encoding="utf-8")
ls = ["中国","法国","英国"]
fo.writelines(ls)
fo.seek(0,0)
for line in fo :
    print(line)
fo.close()


# 写文件：
# a.write(s)
# 向文件写入一个字符串或字节流

# a.writelines(lines)
# 将一个元素全为字符串的列表写入文件
# 元素直接拼接写入文件

# a.seek(offset[, whence])
# 参数：
# offset —— 开始的偏移量，也就是代表需要移动偏移的字节数
# 可正可负，正数表示向后移动offset位，负数表示向前移动offset位
# 可简单使用 a.seek(0) 使文件指针移到文件开头
# 当在中文字符间移动指针时，该参数只能为 0
# 因为该参数为移动的字节数，不能处理 utf-8 编码的汉字
#
# whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
# 0 —— 从文件开头开始算起，
# 1 —— 从当前位置开始算起，
# 2 —— 从文件末尾算起。
# 
# 返回值：
# 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。