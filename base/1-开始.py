"""
    1、任何编程语言都是用来描述数据、处理数据的，python也不例外
    2、python和其他语言不同，定义变量时，无需指定类型，直接写变量名即可
    3、列表用于描述一组有序数据，类似其他语言的数组，即 [xxx,xxx]
"""

# 定义一个变量movies,它执行一个包含3个字符串的列表list
movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life"
]
# 直接打印查看数据
print(movies)

# list的一些常规操作
# 插入数据
movies.insert(1, 1975)
# 追加数据
movies.append("Hello")
# 删除最后一个
movies.pop()
# 删除指定索引
movies.pop(1)


"""
    4、python的for循环形式为 for each_data in data_list:
    5、python不使用其他语言的{}来包裹代码块，而是使用  :和缩进来实现,请仔细观察下面代码的for使用
"""

# 迭代列表
for movie in movies:
    print(movie)

# 定义一个嵌套的列表
movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]
# 遍历打印每一个元素
for movie in movies:
    # 类型判断，isinstance是一个内置函数，list是内置数据类型
    if isinstance(movie, list):
        for m in movie:
            print(m)
    else:
        print(movie)


"""
    6、上面使用了 if 和 else ，同样的，它们的代码块也是用:和缩进实现的
    7、这里未介绍 【else if】的使用，在python中，使用 elif 表示其他语言的else if
    8、isinstance 、list 、 print这些方法或者类型，都是python语言层内置的，可以直接使用
"""
