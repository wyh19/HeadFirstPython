"""
    1、接上一节，需要检查一条语句中是否包含: ,
    2、使用字符串的find函数，如果找不到，则返回 -1；如果找到，则返回改字符的索引
    3、因此判断语句可以写成 if line.find(':') > -1: 
    也可以写成 if not line.find(':') == -1:
"""

data = open('./base/data-file/sketch.txt')

for line in data:
    if line.find(':') > -1:
        (role, spoken) = line.split(':', 1)
        print(role+' said:', end='')
        print(spoken, end='')

data.close()

# 这次不再报错了
