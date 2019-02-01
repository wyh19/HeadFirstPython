"""
    1、本节的任务是将上一节的代码包装一下，包装出一个get_coach_data函数，使其可以可带文件，并直接返回排序后的结果
"""

# 统一数据格式的函数
def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec

# 读取文件数据并排序
def get_coach_data(fileName):
    try:
        with open(fileName) as f:
            data = f.readline().strip().split(',')
        return sorted(set([sanitize(d) for d in data]))[0:3]
    except:
        print('Error')
        return None

print(get_coach_data('./base/data-file/data1/james.txt'))