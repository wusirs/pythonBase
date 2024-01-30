# 数据定义类

class Record:
    def __init__(self, date: str, order_id: str, money: int, province: str) -> None:
        self.date = date  # 订单日期
        self.order_id = order_id  # 订单id
        self.money = money  # 订单金额
        self.province = province  # 销售省份

    def __str__(self):
        return '{date: %s, order_id : %s, money: %d, province: %s}' % \
        (self.date, self.order_id, self.money, self.province)
        # return f'{self.date}, {self.order_id}, {self.money}, {self.province}'
