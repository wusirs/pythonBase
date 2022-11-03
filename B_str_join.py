print("1" + '12')

# 字符串和数字不可以直接加
# print("123" + 1)

name = '张三'
age = 12
salary = 1200
tall = 1.5
message = "我是%s, 今年%s, 工资%d元， 身高%2d.2f米" % (name, age, salary, tall)
print(message)

print(f'我是{name}, 今年{age}, 工资{salary}元， 身高{tall}米')
