# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）

counter = 100
miles = 1000.0
name = "John"


# 二进制转换：
int('10',2)
# > 2
bin(10)
# > '0b1010'
bin(10)[2:]

c = "1"
ord(c) # c为字符
# 返回值：对应的十进制整数（ASCll数值）
int(c) # c为字符，转化为对应的数字

float('-inf') # 最小值
# -inf

a = b = c = 1
a, b, c = 1, 2, "john"

tinylist = [123, 'john', 0]
print(all(tinylist)) # 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

# 从左到右索引默认【0开始的】，最大范围是字符串【长度少1】
# 从右到左索引默认【-1开始的】，最大范围是【字符串开头】
# 第三个参数，参数作用是【截取的步长】
s = "a1a2···an"   # n>=0

# 向上取整：math.ceil()
# 向下取整：math.floor()、整除"//"
# 四舍五入：round()——奇数向远离0取整，偶数去尾取整；或言之：奇数进位，偶数去尾
# 向0取整：int()

print(type('dsaffd'))
print(type(12))