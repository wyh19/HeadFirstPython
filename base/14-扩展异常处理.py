"""
    1、续上一节末尾提到的问题，当使用try-except时，并不能保证文件得到close执行的机会，因此使用try-except-finally，
    将close放在finaly中，确保执行的机会
    2、使用 【 except XXXError as err 】的句式，显示详细错误信息
    3、当文件不存在是，打开文件后的变量file_data是未定义的，如果直接对其操作file_data.close(),会引发异常，
    判断当前模块上下文中是否存在名字为'file_data'的变量
    4、locals()函数返回当前模块的所有变量名
"""

try:
    file_data = open('missing.txt')
    print(file_data.readline())
except IOError as err:
    # 使用str(err)将错误信息转换成字符串
    print('IOError:'+str(err))
finally:
    if 'file_data' in locals():
        file_data.close()
