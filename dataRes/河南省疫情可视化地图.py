import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读文件
f = open('.\国内疫情图.txt', 'r', encoding='utf8')
data = f.read()

# 关闭文件
f.close()

# 获取河南省数据
data_dict = json.loads(data)
cities_data = data_dict['areaTree'][0]['children'][3]['children']

# 准备数据为元组并放入到list
data_list = []
for city_data in cities_data:
    city_name = city_data['name'] + '市'
    city_confirm = city_data['total']['confirm']
    data_list.append((city_name, city_confirm))
# 构建地图
m = Map()
m.add('河南省各市疫情地图', data_list, '河南')

# 设置全局选项
m.set_global_opts(
    title_opts=TitleOpts(
        title='河南省各市疫情地图',
        pos_left='center',
        pos_top='5%'
    ),
    visualmap_opts=VisualMapOpts(
        is_show=False,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[  # 手动设置分段
            {'min': 0, 'max': 9, 'label': '1-9人', 'color': '#CCFFFF'},
            {'min': 10, 'max': 99, 'label': '10-99人', 'color': '#FFFF99'},
            {'min': 100, 'max': 499, 'label': '100-499人', 'color': '#FF9966'},
            {'min': 500, 'max': 999, 'label': '500-999人', 'color': '#FF6666'},
            {'min': 1000, 'max': 9999, 'label': '1000-9999人', 'color': '#CC3333'},
            {'min': 10000, 'label': '10000人以上', 'color': '#990033'},
        ]
    ))

# 绘图
m.render('河南省各市疫情地图.html')
