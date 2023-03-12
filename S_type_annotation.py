# 类型注解，注解类型与实际类型不符时不会报错

# 变量类型注解
# 格式1:基础容器类型 变量名 : 类型
# 格式2：容器类型详细注解 变量名 : 类型[类型1,类型2，，，] （要标记每个元素的类型，有几个数据标记几个，）
import json
import random

var1: int = 10
var2: float = 1.2
var3: bool = True
var4: str = 'hello'

my_list: list[int] = [1, 2, 3]
my_list1: list = [1231, 231]
my_tuple: tuple[str, int, bool] = ('hello', 444, True)
my_set: set[int] = {1, 3, 4}

# 字典[]里面第一个表示的时key，第二个表示的value
my_dict: dict[str, int] = {'a': 1}

# 注解方式二，利用注释进行注解

va1 = random.randint(1, 10)  # type: int
va2 = json.loads('{"name": "张三"}')  # type: dict[str, str]


# print(va2.get('name'))


# 函数方法的类型注解

# 1、对函数形参进行类型注解
def add(x: int, y: int):
    return x + y


add_sum = add(1, 2)


# 2、函数返回值注解
def func(data: list) -> list:
    return data


data1 = func([12, 23])
