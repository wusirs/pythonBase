# list自定义排序方式
my_list = [['a', 4], ['b', 1], ['c', 2]]


def choose_sort_key(element):
    return element[1]


# my_list.sort(key=choose_sort_key, reverse=True)
my_list.sort(key=lambda element: element[1], reverse=False)
print(my_list)
