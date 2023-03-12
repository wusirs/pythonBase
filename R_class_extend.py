# 继承

class Phone:
    IMEI = None
    producer = 'HM'

    def call_by_4g(self):
        print('4g通话')


class NFCReader:
    nfc_type = '第五代'
    producer = 'BM'

    def read_card(self):
        print('NFC读卡')

    def write_write(self):
        print('NFC写卡')


class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print('红外遥控开启')


class Phone2022(Phone):
    face_id = '10001'  # 面部识别

    def call_by_5g(self):
        print('5g通话')


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()


class MyPhone(Phone, NFCReader, RemoteControl):
    # pass 可以使语法不报错
    pass


class XiaoMiPhone(Phone, NFCReader, RemoteControl):
    # 复写父类的成员属性
    producer = '小米'

    def call_by_4g(self):
        # 调用父类成员属性方式一
        print(Phone.producer)
        # 调用父类成员属性方式二
        print(super().producer)
        # 调用父类方法方式一
        Phone.call_by_4g()

        # 调用父类方法方式二
        super().call_by_4g()


my_phone = MyPhone()
my_phone.call_by_4g()
my_phone.read_card()
my_phone.control()

# 多继承时，如果有两个同名的成员属性时，先继承的优先
print(my_phone.producer)

if my_phone:
    pass
