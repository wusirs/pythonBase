# 模块的导入  [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
# 方式一
import time  # 导入time模块（time.py 文件）
# 方式二：
from random import randint
from random import randbytes as rt
from sys import *

# 睡一秒
time.sleep(.1)

# [1-10] 随机
print(randint(1, 10))

# randbytes 接收1个参数, 用于返回指定长度的随机字节数据
print(rt(1))

# sys.path 的方法
print(path)
