money = 50000
name = None


def query(show_header):
    if show_header:
        print("----------查询余额------------")
    print(f"{name}，你好，你的余额剩余：{money} 元")


def saving(num):
    global money
    money += num
    print("------------存款-----------")
    print(f"{name}，你好，你存款{num}元成功。")
    query(False)


def get_money(num):
    global money
    money -= num
    print("------------取款-----------")
    print(f"{name}，你好，你取款{num}元成功。")
    query(False)


def main():
    print("------------主菜单-----------")
    print(f"{name}, 你好，欢迎来到balabala银行，请选择的的操作：")
    print("查询余额[输入1]")
    print("存   款[输入2]")
    print("取   款[输入3]")
    print("退   出[输入4]")
    return input("请输入你的选择：")


if __name__ == "__main__":
    name = input("请输入你的名字：")
    while True:
        keyboard_input = main()
        if keyboard_input == "1":
            query(True)
            continue
        elif keyboard_input == '2':
            saving(int(input("请输入你要存的金额：")))
            continue
        elif keyboard_input == '3':
            get_money(int(input("请输入你要取的金额：")))
            continue
        else:
            print("退出")
            break
