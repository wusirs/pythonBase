list_m = []
list_m.insert(1, 2)
list_m.insert(1, 'a')
list_m.insert(11, 'v')
# print(list_m)

# 获取list长度
len(list_m)

# 索引元素
list_m.index('a')  # index找不到会报错

# 赋值
list_m[2] = 'b'

# append，追加
list_m.append('c')

list_n = ['x', 'y']

# 追加list
list_m.extend(list_n)

# 删除元素
list_m = ['a', 'b', 'c']
# del(list_m[2])
del list_m[2]

# pop， 取出元素并返回
val = list_m.pop(1)

# remove

list_m = ['a', 'b', 'c', 'a', 'b', 'a']

# 删除第一个符合的元素
list_m.remove('a')
# print(list_m)

# 清空列表
list_m.clear()

# 统计元素个数

list_m = ['a', 'b', 'c', 'a', 'b', 'a']

list_m.reverse()
print(list_m)
cut = list_m.count('a')
# print(cut)
