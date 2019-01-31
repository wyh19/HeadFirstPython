"""
    
"""

# 练习range使用
for num in range(4):
    print(num)

# 增加缩进数目的参数
movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]


def print_lol(the_list, level=0):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end="")
            print(item)


print_lol(movies)

# 增加一个控制参数


def print_lol2(the_list, indent=False, level=0):
    for item in the_list:
        if isinstance(item,list):
            print_lol2(item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="")
            print(item)
print_lol2(movies)
print_lol2(movies,True,2)