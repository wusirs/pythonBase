# 异常
try:
    f = open('test1.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print('出现异常，文件不存在，利用w模式打开，创建文件')
    f = open('test1.txt', 'w', encoding='utf-8')

try:
    print(name)
except NameError as e:
    print('出现变量未定义异常')

try:
    1 / 0
except NameError as e:
    print('出现变量未定义异常')
except ZeroDivisionError as e:
    print(e)

try:
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print(type(e), e)

try:
    1 / 0
except Exception as e:
    print(type(e), e)
else:  # else 表示没有出现异常时执行的代码块
    print('else')
finally:  # 有没有异常都会执行的语句
    print('finally')

try:
    i = 1
except Exception as e:
    print(type(e), e)
else:  # else 表示没有出现异常时执行的代码块
    print('else')
finally:  # 有没有异常都会执行的语句
    print('finally')


def func1():
    print('func1 开始执行')
    1 / 0
    print('func1 结束执行')


def func2():
    print('func2 开始执行')
    func1()
    print('func2 结束执行')


def main():
    try:
        func2()
    except Exception as a:
        print(a)


main()
