"""
    1、本节演示list如何排序，python提供两种形式 【 sorted(xx_list) 】 和 【 xx_list.sort() 】
    2、sorted是内置方法，参数为一个list对象，返回一个全新的排好序的list对象
    3、sort是list对象的方法，因此使用形式是 xx_list.sort(),该方法没有返回值，而是直接将xx_list变为排序后的值
    4、两个方法都支持参数 reverse，默认为False,即从小到大排序；当设置为True时，则从大到小排序
"""

with open('./base/data-file/data1/james.txt') as jaf:
    jm_data = jaf.readline().strip().split(',')


"""
 由于文本里故意有不同形式的时间，导致无法正常排序，因此需要先统一格式
 定义sanitize函数，解决格式问题，将 xx-xx  xx.xx xx:xx 统一为xx.xx
"""
def sanitize(time_str):
    if '-' in time_str:
        spliter = '-'
    elif ':' in time_str:
        spliter = ':'
    else:
        return time_str
    (mins, sec) = time_str.split(spliter, 1)
    return mins + '.' + sec


clean_jm_data = []

for d in jm_data:
    clean_jm_data.append(sanitize(d))

print(sorted(clean_jm_data))
# 改变排序方向
print(sorted(clean_jm_data, reverse=True))
