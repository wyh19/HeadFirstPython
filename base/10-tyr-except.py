"""
    1、考虑第9节最后提到的问题，如果不写find来判断不含：的语句，怎么让代码不因为报错而中断
    2、使用python提供的 try-except
    3、pass 为占位符，表示什么也不执行
"""

data = open('./data-file/sketch.txt')

for line in data:
    try:
        (role, spoken) = line.split(':', 1)
        print(role+' said:', end='')
        print(spoken, end='')
    except:
        pass

data.close()

# 是不是不再报错了
