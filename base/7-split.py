"""
    1、在sketch.txt中，所有对话都是 xxx: xx的形式,因此这里有个需求，分隔开说话的人和其说的话
    2、对字符串分割，使用字符串的split()函数，传入分割的字符，比如【 xxx.split(':') 】
    3、这个代码执行会报错，仔细阅读错误信息，下一节继续优化
"""

data = open('./base/data-file/sketch.txt')

for line in data:
    (role, spoken) = line.split(':')
    print(role+' said:', end='')
    print(spoken, end='')

data.close()

# 错误信息：too many values to unpack，值太多了
# 报错原因：有些语句包含2个:  ，当对其执行split时，将得到3段字符串，但是前面的接受器只有2个变量，导致超出
