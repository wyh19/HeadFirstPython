"""
    1、这一节使用内置库os.path，检查文件是否存在，查看文件的绝对路径
    2、使用 【 from 模块 import 函数 】的形式
"""


from os.path import exists, abspath

file_path = './data-file/sketch.txt'
# 打印文件的绝对路径
print(abspath(file_path))
print('----分隔线----')

# 判断文件是否存在
if exists(file_path):
    data = open(file_path)
    for line in data:
        if not line.find(':') == -1:
            (role, spoken) = line.split(':', 1)
            print(role+'said:', end='')
            print(spoken, end='')
    data.close()
else:
    print('The Data file is missing')

# 尝试将file_path的值改成别的
