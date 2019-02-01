"""
    1、这一节练习写文件，将sketch.txt的文本读出并区分出Man和Other Man所说的话，写入到output/data.out文件中
"""

man = []
other = []

try:
    data = open('./data-file/sketch.txt')
    for line in data:
        try:
            (role, spoken) = line.split(':', 1)
            # strip为清除字符串前后的空格
            spoken = spoken.strip()
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                # 这里终于演示到elif了
                other.append(spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')

# 打印 man 和 other两个list
print(man)
print(other)


"""
    2、打开文件时，第二个参数传入 'w'，表示用于写文件
    3、python写文件，可以使用【 xxfile.write(xxx) 】,也可以使用【 print(xxx,file = xxfile) 】
"""
# 使用 print形式写入文件
try:
    out = open('./output/data.out', 'w')
    print(man, file=out)
    print(other, file=out)
    out.close()
except IOError:
    print('File Error!')

# 使用write形式写入文件,注意:write参数需要是字符串形式，所以使用str强制转换
# 末尾加上 \n 的目的是为了让data2.out里的数据和data.out保持一致，因为print默认会给末尾增加\n
try:
    out = open('./output/data2.out', 'w')
    out.write(str(man)+'\n')
    out.write(str(other)+'\n')
    out.close()
except IOError:
    print('File Error!')

# 思考：如果38行代码发生异常，会怎么样？
# 答案：那么会跳过39行和40行，进入42行，那么由于文件close没有执行，导致文件资源没有释放
# 解决办法：使用finally确保必须执行的代码得到执行，代码如下，下一节具体演示

# try:
#     out  = open('./output/data.out','w')
#     print(man,file = out)
#     print(other,file = out)
#     # 注意，下面一行代码挪到了finally中执行
#     # out.close()
# except IOError:
#     print('File Error!')
# finally:
#     out.close()
