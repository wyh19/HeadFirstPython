"""
    1、这一节扩展print_lol函数，给其增加一个参数fh，在执行print函数时，将该参数传递给print的file参数
    2、print的file参数用于指示print输出到屏幕还是到文件，默认值为sys.stdout,即输出到屏幕
"""
import sys


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for line in the_list:
        if isinstance(line, list):
            print_lol(line, indent, level+1, fh)
        else:
            if indent:
                for sta_stop in range(level):
                    print('\t', end='', file=fh)
            print(line, file=fh)


movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]

with open('./base/output/nester_out.txt', 'w') as nester_out:
    print_lol(movies, fh=nester_out)
