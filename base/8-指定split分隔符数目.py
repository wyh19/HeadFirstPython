"""
    1、split可以指定分割符的数目，超出的分隔符将不再进行分割
    2、这个代码执行依然会报错，仔细阅读错误信息，下一节继续优化
"""

data = open('./base/data-file/sketch.txt')

for line in data:
    # 这一节相对于上一节，就修改了下一行
    (role, spoken) = line.split(':',1)
    print(role+' said:', end='')
    print(spoken, end='')

data.close()

# 错误信息：not enough values to unpack，没有足够的值
# 因为有些行的没有：,导致无法分割出两段字符串