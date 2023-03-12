import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts

# 数据处理
f_us = open('美国.txt', 'r', encoding='utf-8')
us_data = f_us.read()


f_jp = open('日本.txt', 'r', encoding='utf-8')
jp_data = f_jp.read()

f_in = open('印度.txt', 'r', encoding='utf-8')
in_data = f_in.read()

# 去除不合json规范的开头
us_data = us_data.replace('jsonp_1629344292311_69436(', '')
jp_data = jp_data.replace('jsonp_1629350871167_29498(', '')
in_data = in_data.replace('jsonp_1629350745930_63180(', '')

# 去除不合json规范的结尾，去掉右括号加分号
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 转json
us_dict = json.loads(us_data)
in_dict = json.loads(in_data)
jp_dict = json.loads(jp_data)

# 获取 trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确诊数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]

# 生成图表

line = Line()  # 构建这线图对象

# 添加x轴
line.add_xaxis(us_x_data)  # 三个国家共用一个x轴

# 添加y轴
line.add_yaxis('美国确诊人数', us_y_data, label_opts=LabelOpts(
    is_show=False  # 设置默认不显示数据
))
line.add_yaxis('日本确诊人数', jp_y_data, label_opts=LabelOpts(
    is_show=False
))
line.add_yaxis('印度确诊人数', in_y_data, label_opts=LabelOpts(
    is_show=False
))

# 设置全局参数
line.set_global_opts(
    title_opts=TitleOpts(
        title='2020年美日印三国确诊人数对比折线图', pos_left='center', pos_bottom='1%'
    )
)

# 调用render方法，生成图表
line.render()

# 关闭文件对象
f_in.close()
f_us.close()
f_jp.close()



