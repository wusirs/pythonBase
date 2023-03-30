# pyecharts python可视化
from pyecharts.charts import Line, Map
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 得到折线图对象
line = Line()

# 添加x轴数据
line.add_xaxis(['China', 'American', 'England'])

# 添加y轴数据
line.add_yaxis('GDP', [30, 20, 10])

# 设置全局配置  详见 https://pyecharts.org/#/zh-cn/global_options
line.set_global_opts(
    title_opts=TitleOpts('GDP展示',
                         pos_left='center',  # 设置标题的离左侧的位置（center 居中）
                         pos_bottom='1%'  # 设置标题离图底部的位置
                         ),
    legend_opts=LegendOpts(is_show=True),  # 展示图例
    toolbox_opts=ToolboxOpts(is_show=True),  # 展示工具箱
    visualmap_opts=VisualMapOpts(is_show=True)  # 展示视觉映射
)

# 生成图表
# line.render()


# 地图构建
map_c = Map()

# 准备数据
data = [
    ('北京', 99),
    ('上海', 199),
    ('台湾', 9),
    ('广东', 321),
    ('安徽', 320)
]

# 设置全局选项
map_c.set_global_opts(visualmap_opts=VisualMapOpts(
    is_show=True,  # 展示视觉映射
    is_piecewise=True,  # 是否分段
    pieces=[  # 开启手动校准视觉映射范围
        {'min': 1, 'max': 9, 'label': '1-9人', 'color': '#CCFFFF'},
        {'min': 10, 'max': 99, 'label': '10-99人', 'color': '#FF6666'},
        {'min': 100, 'max': 500, 'label': '100-500人', 'color': '#990033'},
    ]
))

# 添加数据
map_c.add('测试地图', data, 'china')

# 生成地图
map_c.render()
