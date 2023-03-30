# tuple 一旦定义就不可以被修改

# 定义
tuple_m = ()
tuple_n = ('a', 'b')
# 如果定义单个元素的tuple时，要在单个元素后加一个逗号，否则会被认为是str类型
tuple_o = ('a', )
print(type(tuple_o))
tuple_p = (('a', 'b'), (1, 2))

tuple_a = tuple()
tuple_b = tuple('b')
tuple_c = tuple(tuple_n)

# 获取元素
t1 = ((1, 2, 3), (4, 5, 6))
element = t1[1][2]
# print(element)


# tuple 不可以修改，但是如果tuple有数组，数组可以修改
t2 = ([1, 2, 3], [2, 3, 4])
t2[1][0] = 'a'
print(t2)

