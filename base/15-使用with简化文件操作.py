"""
    1、对于文件的操作，python提供了with语法，简化try-except-finally的固有模式
    2、语法形式为 【 with open(xxx) as xx_file 】
    3、对整个with包上try-except即可处理期间的异常，with会自动帮你关闭文件
"""

try:
    with open('missing.txt') as data:
        print(data.readline())
except IOError as err:
    print('File Error:'+str(err))