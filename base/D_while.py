import random

i = 1
sum_i = 0
while i <= 100:
    sum_i += i
    i += 1
print(f'1~100累加之和是：{sum_i}')


# randint = random.randint(1, 100)
# count = 0
# flag = True
# while flag:
#     guess_num = int(input("请输入你要猜的数字："))
#     count += 1
#     if guess_num == randint:
#         flag = False
#     else:
#         if guess_num > randint:
#             print("猜大了！")
#         else:
#             print("你猜小了！")
#
# print(f"总共猜了{count}次")

# 打印九九乘法表
i, j = 1, 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j}×{i} = {j * i}\t", end=" ")
        j += 1
    print("")
    i += 1
