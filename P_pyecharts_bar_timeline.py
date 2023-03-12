# 时间线柱状图
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 柱状图
bar1 = Bar()
bar1.add_xaxis(['China', 'American', 'England'])
bar1.add_yaxis('GDP', [30, 20, 10], label_opts=LabelOpts(
    position='right'  # 修改数值标签位置，反转柱状图时使用
))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['China', 'American', 'England'])
bar2.add_yaxis('GDP', [50, 40, 20], label_opts=LabelOpts(
    position='right'  # 修改数值标签位置，反转柱状图时使用
))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['China', 'American', 'England'])
bar3.add_yaxis('GDP', [60, 45, 40], label_opts=LabelOpts(
    position='right'  # 修改数值标签位置，反转柱状图时使用
))
bar3.reversal_axis()

# 创建时间线，并设置主题
timeline = Timeline({'theme': ThemeType.LIGHT})

# 自动播放
timeline.add_schema(
    play_interval=1000,  # 自动播放时间线的间隔时间（单位毫秒）
    is_timeline_show=True,  # 是否展示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否循环播放
)

# 绘图
timeline.add(bar1, '2022年GDP')
timeline.add(bar2, '2023年GDP')
timeline.add(bar3, '2024年GDP')

# 通过时间线绘图
timeline.render()
