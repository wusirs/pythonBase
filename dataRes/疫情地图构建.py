from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts, LabelOpts
import json

f = open('国内疫情图.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
data_dict = json.loads(data)

# 从字典中取省份数据
province_data_list = data_dict['areaTree'][0]['children']

# 从字典中取出每个省份和确诊人数为元组，组装成一个新的列表
data_list = []  # 绘图需要用的数据列表
for province_data in province_data_list:
    province_name = province_data['name']  # 省份名称
    province_confirm = province_data['total']['confirm']  # 确诊人数
    data_list.append((province_name, province_confirm))

# 构建地图
m = Map()

# 添加数据
m.add('各省份确诊人数', data_list, 'china', label_opts=LabelOpts(is_show=True, font_size=8))

# 设置全局配置，定制分段视觉映射
m.set_global_opts(
    title_opts=TitleOpts(
        title='全国疫情地图',
        pos_left='center',
        pos_top='5%'
    ),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[  # 手动设置分段
            {'min': 1, 'max': 9, 'label': '1-9人', 'color': '#CCFFFF'},
            {'min': 10, 'max': 99, 'label': '10-99人', 'color': '#FFFF99'},
            {'min': 100, 'max': 499, 'label': '100-499人', 'color': '#FF9966'},
            {'min': 500, 'max': 999, 'label': '500-999人', 'color': '#FF6666'},
            {'min': 1000, 'max': 9999, 'label': '1000-9999人', 'color': '#CC3333'},
            {'min': 10000, 'label': '10000人以上', 'color': '#990033'},
        ]
    )
)

# 生成国内地图
m.render()
