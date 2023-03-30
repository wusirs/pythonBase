# 测试自定义包，自定义模块
import N_my_module   # 在import模块时会执行该模块里的代码
from myPackage import myModule
from myPackage.cusModule import reduce

print(N_my_module.add(1, 1))
print(N_my_module.divisor(1, 2))
print(myModule.multiply(1, 2))
print(reduce(1, 2))