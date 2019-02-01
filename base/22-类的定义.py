""" 
    1、本节演示类的定义，所谓类就是代码对现实世界的一种模拟，
    比如定义一个动物类，表示动物这么一类事物；
    当对类进行实例化（传入参数执行）之后，才得到一只具体的动物；
    这只具体的动物是一个实体对象，表示动物类的一个实例
    2、python 中的类定义形式如下所示：
    【
        class Xxxx:
            def __init(self,xxxxx):
                xxxxx
            def xxx(self,xxxxx)
                xxxxx
     】
    3、每个类都有一个构造函数 __init__
    4、每个函数第一个参数必须是 self，表示实例化的对象
    5、实例化操作不需要写new (其他语言大多是new Xxx()形式)，
       python的实例化对象的操作为  xx = Xxxx(参数1，参数2...),xx为实例化的对象
    6、类的名字首字母要求大写（其他语言也是如此），
"""


class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def hello(self):
        print('我是一只'+self.type+'，我的名字叫'+self.name)


d = Animal(name='旺财', type='小狗')
d.hello()
