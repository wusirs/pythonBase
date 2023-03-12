# 自定义模块

# from 模块名 import *， import模块时只能import到__all__ 里面定义的方法
__all__ = ['add']


def add(a, b):
    print('add 方法被执行')
    return a + b


def divisor(a, b):
    return a / b


# add(1, 2)  # 这个在import模块时会被执行，调用add方法

if __name__ == '__main__':  # 这个方法在import模块时不会被执行
    add(1, 2)
