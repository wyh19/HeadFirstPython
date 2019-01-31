"""set用于创建一个没有重复项的列表"""



# 下面是接demo18
with open('./book-source/hfpy_ch5_data/james.txt') as jaf:
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


print(sorted(set([sanitize(d) for d in jm_data]))[0:3])
