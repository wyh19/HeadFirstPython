"""
    1、使用open打开文件
    2、xxfile.readline()读取行
    3、xxfile.seek(index)将光标移到某个索引位置
    4、close()关闭文件
"""


the_file = open('./base/data-file/sketch.txt')
"""
上面的文件路径是相对路径，但是根据我的编程经验，应该是 ./data-file/sketch.txt，但是不对
猜测py文件被执行时，提升到根目录了，所以其同级目录是base
只是猜测，不要纠结这个问题
"""

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
