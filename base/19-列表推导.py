"""
1、还记得上一节的下述代码吗？
clean_jm_data = []
for d in jm_data:
    clean_jm_data.append(sanitize(d))
在python中，可以使用列表推导形式，解决这种简单的列表转化
形式为：【   [ xxx(item) for item in xx_list ]  】

"""


with open('./data-file/data1/james.txt') as jaf:
    jm_data = jaf.readline().strip().split(',')


def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec


print(sorted([sanitize(d) for d in jm_data]))
# 如果觉得上面的代码有点吓人，分解为下面两句，习惯就好了
# clean_jm_data = [sanitize(d) for d in jm_data]
# print(sorted(clean_jm_data))
