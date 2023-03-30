from typing import Union

# 联合注解


# list[Union[str, int]] list中的元素有str和int这两种类型
my_list: list[Union[str, int]] = [1, 2, '123', 'abc']

# dict[str, Union[str, int]] key是str，value是str或int
my_dict: dict[str, Union[str, int]] = {'name': '张三', 'age': 12}


def func(data: Union[int, str]) -> Union[int, str]:
    pass
