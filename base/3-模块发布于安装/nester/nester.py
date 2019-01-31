""" 这里的注释是模块说明 """


def print_lol(the_list):
    """ 这里的注释是函数的说明：递归打印嵌套list """
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
