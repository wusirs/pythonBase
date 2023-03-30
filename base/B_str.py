str1 = 'my name is july'

#
print(str1[5])
print(str1[-1])

print(str1.index('m', 2, 10))

# replace 不修改原字符串，返回一个新的字符串
str2 = str1.replace('m', 'n')
print(str2)

# split
str1 = '  my name is july  '
str1_list = str1.split(' ')
print(str1_list)

# 首位去除
str1 = '11aabb11'
strip = str1.strip('1')
strip = str1.lstrip('1')
strip = str1.rstrip('1')
print(strip)

# 首位填充
str2 = '1112'
str3 = str2.rjust(10, '0')
print(str3)
# str2.ljust()


# find
str4 = 'sfjaldfjaljf'
print(str4.rfind('a'))
print(str4.find('a'))

# 统计
count = str4.count('a')
print(count)


str_a = 'a1 = {} a2= {}  a3= {}'
a_format = str_a.format('first', 'second', 'third')
print(a_format)

str_b = 'a1 = {1} a2= {0}  a3= {2}'
b_format = str_b.format('first', 'second', 'third')
print(b_format)


