def print_file_info(path):
    f = None
    try:
        f = open(path, 'r', encoding='utf-8')
        # print(f.read())
    except FileNotFoundError as fe:
        print("文件不存在")
    else:
        print(f.read())
    finally:
        if f:
            f.close()


def append_to_file(path, data):
    f = None
    f = open(path, 'a', encoding='utf-8')
    # f.write(dataRes)
    f.write(data)
    if f:
        f.close()


if __name__ == '__main__':
    append_to_file('test.txt', 'hello\nworld\n')
    print_file_info('test.txt')