# 序列（list, tuple, str）

# 切片，切片不影响原序列，而是会生成一个新的序列并返回
# 序列[起始下标:结束下标:步长]
# 起始下标不写表示从0开始，结束下标不写表示到结尾，步长不写表示步长为1
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[3:1:-1])
list2 = list1[::2]
print(list2)

print('12345678'[::-1])
print('0123456'[3:1:-1])

t1 = (0, 1, 2, 3, 4, 5, 6)
print(t1[::-2])

# 案例 获取 '黑马程序员' 字符串
str1 = '万过薪月，员序程马黑来，nohtyP学'
index1 = str1.index('黑')
index2 = str1.index('员')
# print(index2, index1)
print(str1[index1:index2 - 1:-1])

print(str1.split('，')[1].replace('来', '')[::-1])
str2 = str1[::-1]
print(str2[str2.index('黑'): str2.index('员') + 1])

