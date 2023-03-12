#  进行数据计算

from file_define import *
from data_define import *
from pyecharts.charts import Line
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader('2011年1月销售数据.txt')
json_file_reader = JsonFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.analysis_data()
feb_data: list[Record] = json_file_reader.analysis_data()

# 将两个月的数据合并
all_data: list[Record] = jan_data + feb_data

# 进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有数据了，所以和老数据做累加
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
line = Line(init_opts=InitOpts(theme=ThemeType.LIGHT))


#  可以先根据data_dict.keys() sorted排序一下
line.add_xaxis(list(data_dict.keys()))

line.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(
        title='每日销售额'
    )
)

line.render('每日销售额折线图.html')
