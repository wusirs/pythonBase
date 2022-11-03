# 容器的通用操作

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdfeg"
my_set = {1, 2, 3, 4, 5}
my_dict = {1: 'a', 2: 'b', 3: 'c'}

# len
print(len(my_dict))

# max
print(max(my_dict))


# min
print(min(my_str))

# sorted(容器,[reverse=True])，排序之后返回列表对象
l = sorted(my_dict, reverse=True)
print(f'排序：{l}')

# 容器之间的转换 , 无法转字典
print(list(my_dict))
print(list(my_set))

print(tuple(my_dict))
print(tuple(my_str))

print(str(my_dict))
print(str(my_tuple))
print(str(my_list))

print(set(my_dict))
