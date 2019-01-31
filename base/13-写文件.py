"""
    1、这一节练习写文件，将sketch.txt里的文本
"""

man = []
other = []

try:
    data = open('./base/data-file/sketch.txt')
    for line in data:
        try:
            (role, spoken) = line.split(':', 1)
            spoken = spoken.strip()
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')

print(man)
print(other)

#开始写入文件
try:
    out  = open('./base/output/data.out','w')
    print(man,file = out)
    print(other,file = out)
    out.close()
except IOError:
    print('File Error!')

# 思考：如果28行代码发生异常，会怎么样？
# 答案：那么会跳过29行和30行，进入32行，那么由于文件close没有执行，导致文件资源没有释放
# 解决办法：使用finally确保必须执行的代码得到执行

# try:
#     out  = open('./base/output/data.out','w')
#     print(man,file = out)
#     print(other,file = out)
#     # 注意，下面一行代码挪到了finally中执行
#     # out.close()
# except IOError:
#     print('File Error!')
# finally:
#     out.close()
