tinylist = [123, 'john']
# print(tinylist[0])  # 输出列表的第一个元素
# print(tinylist[1:3])  # 输出第二个至第三个元素
# print(tinylist[2:])  # 输出从第三个开始至列表末尾的所有元素

# 二维数组
num_list = [[0] * 5 for i in range(5)]
n, m = 4, 6
dp = [[1]*n] + [[1]+[0] * (n-1) for i in range(m-1)]
# print(num_list)
# print(dp)