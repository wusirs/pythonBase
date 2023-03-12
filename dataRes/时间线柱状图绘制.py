#  绘制时间线动态柱状图

# 读取文件
import pyecharts.charts
from pyecharts.globals import ThemeType

f = open('1960-2019全球GDP数据.csv', 'r', encoding='gb2312')
data_lines = f.readlines()
f.close()

# 删除第一行数据
data_lines.pop(0)

# print(float('5.433E+11'))

# 将数据转换为字典存储，格式为
# {年份:[[国家,gdp], [国家,gdp]....]}
data_dict = {}
for line in data_lines:
    year = int(line.split(',')[0])  # 年份
    country = line.split(',')[1]  # 国家
    gdp = float(line.split(',')[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError as e:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 排序字典的key（年份）
sorted_year_list = sorted(data_dict.keys())

# 创建时间线对象
timeline = pyecharts.charts.Timeline({'theme': ThemeType.LIGHT})

for year in sorted_year_list:
    #  按照gdp由高到低排序
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年gdp前八的国家
    year_data = data_dict[year][0:8]
    # 构建柱状图
    x_data = []  # x轴数据
    y_data = []  # y轴数据
    for country_gdp in year_data:
        # print(country_gdp)
        x_data.append(country_gdp[0])  # x轴添加国家数据
        y_data.append(country_gdp[1] / 100000000)  # y轴添加gdp数据

    # 构建柱状图对象
    bar = pyecharts.charts.Bar()

    # 再次反转列表中的数据把gdp高的放在上面
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)', y_data, label_opts=pyecharts.options.LabelOpts(
        position='right'
    ))

    # 反转x，y轴
    bar.reversal_axis()

    # 设置每一年图标的标题
    bar.set_global_opts(title_opts=pyecharts.options.TitleOpts(
        title=f'{year}年全球GDP前八数据'
    ))

    # 将bar对象添加到时间线中
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 绘图
timeline.render('1960-2019全球GDP前八国家.html')
