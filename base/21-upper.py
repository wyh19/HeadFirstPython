def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec


def get_coach_data(fileName):
    try:
        with open(fileName) as f:
            data = f.readline().strip().split(',')
        return sorted(set([sanitize(d) for d in data]))[0:3]
    except:
        print('Error')
        return None

print(get_coach_data('./book-source/hfpy_ch5_data/james.txt'))