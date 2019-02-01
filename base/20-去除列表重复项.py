"""
    1、本节的目的是实现列表的去重以及取前3个值
    2、去重使用 set(xxx_list),得到一个去重后的集合,
    3、python的集合是{}形式的
    4、对集合排序，得到一个list
    5、取集合的前几项使用【 xx_list[x:y] 】形式，x为开始的索引，y为结束的索引（不包括）
"""
# 仔细观察下面的输出
print(set([1, 3, 2, 1, 3, 4, 6, 5]))
print(sorted(set([1, 3, 2, 1, 3, 4, 6, 5])))
print(sorted(set([1, 3, 2, 1, 3, 4, 6, 5]))[1:4])

with open('./base/data-file/data1/james.txt') as jaf:
    jm_data = jaf.readline().strip().split(',')


def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec


# 仔细分解下面的语句
print(sorted(set([sanitize(d) for d in jm_data]))[0:3])
