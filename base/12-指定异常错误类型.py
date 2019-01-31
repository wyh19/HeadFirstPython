"""
    1、这一节演示指定特定的异常类型，当指定异常类型时，该except语句只会捕获该类型的异常
"""

try:
    data = open('./file/sketch.txt')
    for line in data:
        try:
            (role, spoken) = line.split(':', 1)
            print(role+' said:', end='')
            print(spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The Data is missing')
