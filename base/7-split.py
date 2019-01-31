"""在6中，所有对话都是 xxx: xx的形式"""

data = open('./file/sketch.txt')

for line in data:
    (role, spoken) = line.split(':')
    print(role+' said:', end='')
    print(spoken, end='')

data.close()

# 会发现当出现多个：时，导致值过多的错误,那么限制split的分割数目,见demo8

