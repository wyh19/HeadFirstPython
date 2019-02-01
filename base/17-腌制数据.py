
"""
    1、上一节介绍了将list数据写入文件，思考一下，如果要读取回来，数据应该是字符串，还要转化为list，比较麻烦；
        这一节，介绍python的一个内置的数据写入文件与原样读取的办法，即“腌制数据”
    2、使用内置库pickle, pickle.dump为写入数据， pickle.load为读取数据
    3、使用腌制数据，文件的读写要使用二进制形式，即 wb 和rb
"""

import pickle

movies = [
    "The Holy Grail",
    "The Life of Brian",
    "The Meaning of Life",
    [
        "Machael Palin",
        "John CLeeses"
    ]
]

# dump数据，使用wb模式，即二进制写入文件
with open('./output/dump.pickle', 'wb') as mySavedData:
    pickle.dump(movies, mySavedData)

# load数据，数据原样读出
with open('./output/dump.pickle', 'rb') as myRestoredData:
    movies2 = pickle.load(myRestoredData)

# 打印读取的数据
print(movies2)
# 比较读取回来的数据是否等于之前的
print(movies2 == movies)
# 比较二者是不是同一个数据
print(movies2 is movies)
