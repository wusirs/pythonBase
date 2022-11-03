# set 元素不重复，不支持下标索引，不可以用while循环遍历

# s1 = {} # 注意定义空set不可以用这个，这个定义的是字典
s2 = {'1', '2', 'a', '1'}
s3 = set('1')

print(s2)

# 添加元素 add
sa = set()
sa.add('1')

# remove 移除元素，找不到抛异常
sa.remove('1')

# pop 随机去除一个元素
sa = {'1', '2', 'a', 'b'}
ele = sa.pop()
print(ele)

# clear 清空
sa.clear()

# difference 取集合的差集，不影响原有的两个集合
sm = {1, 2, 3}
sn = {2, 3, 7}
print(sm.difference(sn))
print(sn.difference(sm))

# 集合1.difference_update(集合2) 在集合1内删除和集合2相同的元素，改变集合1
sm.difference_update(sn)
print(sm, sn)

# union 集合合并，不影响原来的两个集合
sm = {1, 2, 3}
sn = {2, 3, 7}
union = sm.union(sn)
print(sm, sn, union)

# len
len(union)

# 集合的遍历
for item in union:
    print(item, end=', ')

