"""
    1、在6中，所有对话都是 xxx: xx的形式,因此这里有个需求，分隔开说话的人和其说的话
    2、对字符串分割，使用字符串的split()函数，传入分割的字符，比如【 xxx.split(':') 】
    3、
"""

data = open('./base/data-file/sketch.txt')

for line in data:
    (role, spoken) = line.split(':')
    print(role+' said:', end='')
    print(spoken, end='')

data.close()

# 会发现当出现多个：时，导致值过多的错误,那么限制split的分割数目,见demo8
