# 自定义字符串的反转
def str_reverse(s):
    # res = ''
    # for i in s:
    #     res = i + res
    # return res
    return s[::-1]


#  自定义字段串截取
def substr(s, x, y):
    res = ''
    index = 0
    while True:
        if x <= index < y:
            res += s[index]

        if index >= y:
            break
        index = index + 1
    # return res
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse('dfafasfj'))
    print(substr('dfasjdfsa', 1, 4))