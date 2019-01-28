"""14节中的模式,可以使用with语法专门处理"""

try:
    with open('missing.txt') as data:
        print(data.readline)
except IOError as err:
    print('File Error:'+str(err))