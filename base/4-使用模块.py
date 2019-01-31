"""
    1、导入模块，使用【 import 模块名】的形式
    2、由于nester在第3步中是安装到本地的，所以直接【 import nester 】可以找到它
    3、要使用模块里的函数或者数据变量，使用【 模块.xxx 】得到，比如下面的 【nester.print_lol()】
"""

import nester

movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]

nester.print_lol(movies)


"""
    4、也可以使用【 from 模块  import 函数名称 】,直接使用模块里的函数，样例为下面注释掉的代码
"""
# from  nester import print_lol
# print_lol(movies)