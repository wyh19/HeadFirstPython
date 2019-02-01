"""
    1、这里介绍类的继承，继承是一种代码复用的形式，思考下，之前设计Athlete类，主要目的是为了计算运动员的成绩单（list数据），
    因此可以考虑定义一个list类的子类，该子类扩展了list没有的功能，比如运动员的姓名，比赛日期，获取前3成绩的方法
    2、定义继承类的格式如下：
    【
        class  Xxx(Yyy):
            def __init__(self,xx):
                Yyy.__init__()
                self.xx = xx
                ...
            def 其他函数:
                ...
     】
"""

# 这个代码之前看过多次，这里可以忽略


def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec

# 使用继承的形式定义运动员类，注意和之前的比较


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        # 下面这行是比之前多出来的，用于构造父类的数据
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        # 下面这句和之前不同，之前是定义一个属性来保存成绩单，现在这个类自身就是list的一个子类，因此自身即可扩展列表数据
        self.extend(a_times)

    def top3(self):
        # 下面这句和之前也不同，直接使用self获取成绩单数据
        return sorted(set([sanitize(t) for t in self]))[0:3]


# 一些测试，证明AthleteList具有list的所有特征
vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())

# 和之前没有变化


def get_coach_data(fileName):
    try:
        with open(fileName) as f:
            data = f.readline().strip().split(',')
        return AthleteList(data.pop(0), data.pop(0), data)
    except IOError as err:
        print('Error'+str(err))
        return None


james = get_coach_data('./data-file/data2/james.txt')
result = james.top3()
print(result)
