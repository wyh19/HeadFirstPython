"""

"""

movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life"
]
print(movies)

# 插入数据
movies.insert(1, 1975)
# 追加数据
movies.append("Hello")
# 删除最后一个
movies.pop()
# 删除指定索引
movies.pop(1)


# 迭代
for movie in movies:
    print(movie)

movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]
for movie in movies:
    # 类型判断
    if isinstance(movie, list):
        for m in movie:
            print(m)
    else:
        print(movie)
