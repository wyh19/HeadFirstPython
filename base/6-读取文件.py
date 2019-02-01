"""
    1、使用open打开文件
    2、xxfile.readline()读取行
    3、xxfile.seek(index)将光标移到某个索引位置
    4、close()关闭文件
"""

the_file = open('./data-file/sketch.txt')


# 打印第一行，光标移到第一行结束
print(the_file.readline(), end='')
# 打印第二行
print(the_file.readline(), end='')

# 分隔线，便于看清楚
print('----以上只是练习-----')

# 光标回到文件的第一行开始
the_file.seek(0)

# 依次打印每一行数据
for line in the_file:
    print(line, end='')

# 关闭文件
the_file.close()
