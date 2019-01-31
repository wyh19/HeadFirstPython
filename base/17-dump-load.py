
"""上一节介绍了将list数据写入文件，思考一下，如果要读取回来，是不是比较麻烦
这一节，介绍python的一个内置的数据写入文件与原样读取的办法，即“腌制数据”
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
with open('./file/dump.pickle', 'wb') as mySavedData:
    pickle.dump(movies, mySavedData)

# load数据，数据原样读出
with open('./file/dump.pickle', 'rb') as myRestoredData:
    movies2 = pickle.load(myRestoredData)

print(movies2)
print(movies2 == movies)
print(movies2 is movies)

