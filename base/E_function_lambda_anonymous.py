# lambda 匿名函数，无名称只可以临时使用

# lambda函数定义: lambda 参数（多个逗号分隔） : 函数体（只能有一行）


def test_function(compute):
    result = compute(1, 2)
    print(result)


# 函数体计算结果默认return
test_function(lambda x, y: x + y)

print(test_function.__name__)