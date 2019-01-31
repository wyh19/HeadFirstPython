""" 
    1、函数（或者成为方法），就是一段可以调用的代码
    2、函数一般由函数名、参数、函数体、返回值（可省略，则返回None,即无返回值）组成，python定义函数的关键字是 def，因此形式是 
        def func_name(param,xxx):
            代码语句1
            代码语句2...
            return ...
"""
movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]


def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            #函数内调用自己，形成递归调用，由于有if判断的存在，不用担心导致死循环
            print_lol(item)
        else:
            print(item)


# 使用自定义的print_lol函数
print_lol(movies)

## !注意:第3节介绍模块的发布与安装，需要一个文件夹，因此请移步  3-模块发布于安装