def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]


def get_coach_data(fileName):
    try:
        with open(fileName) as f:
            data = f.readline().strip().split(',')
        return Athlete(data.pop(0), data.pop(0), data)
    except IOError as err:
        print('Error'+str(err))
        return None


james = get_coach_data('./book-source/hfpy_ch6_data/james2.txt')
result = james.top3()
print(result)
