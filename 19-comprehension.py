"""这一节演示列表推导(list comprehension)"""
with open('./book-source/hfpy_ch5_data/james.txt') as jaf:
    jm_data = jaf.readline().strip().split(',')

def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins,sec) = time_str.split(spliter,1)
    return mins + '.' + sec

# clean_jm_data = [sanitize(d) for d in jm_data]

# print(sorted(clean_jm_data))

print(sorted([sanitize(d) for d in jm_data]))