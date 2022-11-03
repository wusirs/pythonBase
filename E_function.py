def greatest_common_divisor(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b)


def greatest_common_divisor_one(i, j):
    i = max(i, j)
    j = min(i, j)
    t = 0
    while i % j != 0:
        t = i % j
        i, j = j, i % j
    return t


def greatest_common_divisor_two(p, q):
    p, q = max(p, q), min(p, q)
    t = p - q
    while q != t:
        p, q = max(q, t), min(q, t)
        t = m - n
    return t


money = 12
name = "lisi"


# global 关键字可以将函数内部的局部变量定义为全局变量，这样就可以在函数内部修改全局变量了，不加global定义只可以访问
def test():
    global money
    money += 12
    global name
    name += " is a women"
    print(money, name)


if __name__ == "__main__":
    m, n = 32, 24
    print(f"{m} , {n} 的最大公约数为：%d" % (greatest_common_divisor(m, n)))
    print(f"{m} , {n} 的最大公约数为：%d" % (greatest_common_divisor_one(m, n)))
    print(f"{m} , {n} 的最大公约数为：%d" % (greatest_common_divisor_two(m, n)))
    test()
