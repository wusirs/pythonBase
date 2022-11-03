# pop
d1 = {1: 'a', 2: 'b'}
pop = d1.pop(1)
print(d1)

# clear
d1.clear()

da = {'1': 'a', '2': 'b', 1: 'a'}
db = {1: 'a', 2: 'b'}
print(da)

# get(key) ， key不存在返回None
val = da.get('1')

print(da.values())  # <class 'dict_values'>
print(da.items())  # <class 'dict_items'>  每个item 是 tuple类型
print(da.keys())  # <class 'dict_keys'>

score1 = {'李四': {'语文': 23, '数学': 23}, '张三': {'语文': '100', '数学': '100'}}
for key in score1:
    print(f' {key} :  {score1[key]}')


# len
len(score1)
