with open('./book-source/hfpy_ch5_data/james.txt') as jaf:
    jm_data = jaf.readline().strip().split(',')
    
#由于文本里故意有不同形式的时间，导致无法正常排序，因此需要先统一格式

def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins,sec) = time_str.split(spliter,1)
    return mins + '.' + sec

clean_jm_data = []

for d in jm_data:
    clean_jm_data.append(sanitize(d))

print(sorted(clean_jm_data))