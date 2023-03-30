#  class对象
from typing import Any


class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self, msg):
        print(f'嗨，大家好，我是{self.name}，{msg}')


student = Student()
student.name = '张三'
student.gender = '男'
student.age = 12
student.nationality = '中国'
student.native_place = '安徽'

student.say_hi('很高心认识大家！')


# 闹钟
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock = Clock()
clock.id = 123
clock.price = 19.19


# clock.ring()


class People:
    # 可以省略
    # name = None
    # age = None
    # tel = None

    # 创建对象时自动执行
    def __init__(self, name, age, tel) -> None:
        self.name = name
        self.age = age
        self.tel = tel

    # 相当于java的tostring()
    def __str__(self):
        return f'People类对象，姓名{self.name}，年龄{self.age}岁'

    # 比较，小于或大于
    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.tel == other.tel

    # 比较小于等于或大于等于
    def __le__(self, other):
        return self.age <= other.age


people = People('张三', 14, '13546562564')
people2 = People('张三', 14, '13546562564')
people1 = People('张三', 15, '13546562564')
print(people < people1)
print(people == people2)
print(people1 >= people)


# 私有成员变量，私有成员方法


class Phone:
    __current_voltage = 0.5  # 当前运行电压

    def __keep_single_core(self):
        print('让cpu以单核模式运行')

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print('5G通过已经开启')
        else:
            self.__keep_single_core()
            print('电量不足，无法使用5G通话，并已设置为单核运行进行省电')


phone = Phone()
phone.call_by_5G()