""" 
练习class
构造函数为__init__
每个函数第一个参数必须为self
"""


class Athlete:
    def __init__(self, value=0):
        self.thing = value

    def how_big(self):
        return len(self.thing)


d = Athlete('Holy Grail')
print(d.how_big())
