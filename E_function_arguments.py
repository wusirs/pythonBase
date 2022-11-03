# 函数的传参方式


# 缺省参数，默认参数要定义到最后面，传参时也要放到最后面传
def user_info1(name, age, gender='男'):
    return f'你的名字{name}， 你的年龄{age}， 你的性别{gender}'


print(user_info1('王二', 12, '女'))


# 不定长参数
# 位置不定长，元组
def user_info2(*args):
    print('args类型：', type(args))


user_info2('123', 123)


# 关键字不定长，字典
def user_info3(**kwargs):
    print('kwargs类型', type(kwargs))


user_info3(name='TOM', age=12)


def user_info(name, age, gender):
    return f'你的名字{name}， 你的年龄{age}， 你的性别{gender}'


# 位置传参
print(user_info('张三', 12, '男'))

# 关键字传参
print(user_info(name='张三', gender='男', age=12))

# 位置传参，关键字传参 混用，混用时位置参数要放最前面
print(user_info('张三', gender='男', age=12))
