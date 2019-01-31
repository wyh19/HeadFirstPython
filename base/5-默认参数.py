"""
    1、本节目的是通过扩展参数来增强自定义的print_lol函数
    2、先做个小练习，使用【 for xx in range() 】
"""

# 练习range使用
for num in range(4):
    print(num)

# 要打印的list数据
movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]

"""
    3、增加level参数，使得打印list数据时，嵌套的list数据能按层级缩进
    4、给level参数设置默认值0
"""


def print_lol(the_list, level=0):
    for item in the_list:
        if isinstance(item, list):
            # 下一层级，level要+1
            print_lol(item, level+1)
        else:
            # 打印level个数目的tab字符，形成缩进
            for tab_stop in range(level):
                # 注意：print默认行为是打印完换行，现在指定其end参数为空字符串，即打印完不换行
                print("\t", end="")
            # 打印文字本身
            print(item)


# 使用形式1:不传level，使用其默认值
print_lol(movies)
# 使用形式2:传入level
# print_lol(movies,2)


"""
    5、再增加一个参数，用于控制是否启用嵌套，即下面的indent参数，默认值为False
    6、注意：python的布尔值为 【 True 】和【 False 】,与或非的逻辑运算符为【 and 】【 or 】【 not 】
"""


def print_lol2(the_list, indent=False, level=0):
    for item in the_list:
        if isinstance(item, list):
            print_lol2(item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="")
            print(item)


# 使用形式1
print_lol2(movies)

# 使用形式2,按顺序依次传参
# print_lol2(movies, True, 2)

# 使用形式3,通过指定参数名传参
# print_lol2(movies, indent=True, level=2)
