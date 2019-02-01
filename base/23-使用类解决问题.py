"""
    1、本节的任务是定义一个运动员类Athlete,其有3个属性和1个方法
"""


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


james = get_coach_data('./base/data-file/data2/james.txt')
result = james.top3()
print(result)
