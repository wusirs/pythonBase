# 匿名函数
def test_func(compute):
    result = compute(1, 2)
    print(result)
    print(type(compute))
    print(compute.__name__)


def division(a, b):
    return a / b


def multiplication(a, b):
    return a * b


operator = 'multiplication'

if operator == 'division':
    test_func(division)
else:
    test_func(multiplication)
