# 文件相关类定义
import json

from data_define import Record
from 数据分析案例.data_define import Record


# 定义一个抽象类用来做顶层设计，确定有哪些功能需要实现

class FileReader:
    lines: list[str] = None

    def __init__(self, path):
        self.path = path

    def read_data(self):
        """读取文文件，lines方法把每一行数据放到self.lines中"""
        try:
            f = open(self.path, 'r', encoding='utf8')
            self.lines = f.readlines()
            f.close()
        except FileNotFoundError as e:
            print('文件不存在')

    def analysis_data(self) -> list[Record]:
        """读到的每一条数据都转换为Record对象，将他们都封装到list内返回即可"""
        pass


class TextFileReader(FileReader):

    def analysis_data(self) -> list[Record] | None:
        try:
            self.read_data()
            record_list: list[Record] = []
            for line in self.lines:
                line.strip()
                data = line.split(",")
                record_list.append(Record(data[0], data[1], int(data[2]), data[3]))
            return record_list
        except ValueError as e:
            print('存在销售额数据不是整数格式')
            return None
        except IndexError as e:
            print('下标越界异常')
            return None
        except Exception as e:
            print('未知异常')
            return None


class JsonFileReader(FileReader):

    returnType = list[Record] | None

    def analysis_data(self) -> returnType:
        try:
            self.read_data()
            record_list: list[Record] = []
            for line in self.lines:
                data_dict = json.loads(line)
                record_list.append(
                    Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province']))
            return record_list
        except ValueError as e:
            print('存在销售额数据不是整数格式')
            return None
        except KeyError as e:
            print('key不存在')
            return None
        except Exception as e:
            print('未知异常')
            return None


if __name__ == '__main__':
    list1 = TextFileReader('2011年1月销售数据.txt').analysis_data()
    print(list1)
    list2 = JsonFileReader('2011年2月销售数据JSON.txt').analysis_data()
    print(list2[0])
