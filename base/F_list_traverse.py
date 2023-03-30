# 列表遍历
list_m = ['a', 'b', 'c']

# while 遍历
index = 0
while index < len(list_m):
    element = list_m[index]
    print(element, end=', ')
    index += 1
print()

# for 遍历
for element in list_m:
    print(element, end=', ')
