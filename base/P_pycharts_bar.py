from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 柱状图
bar = Bar()

# 添加x轴
bar.add_xaxis(['China', 'American', 'England'])

# 添加y轴
bar.add_yaxis('GDP', [30, 20, 10], label_opts=LabelOpts(
    position='right'  # 修改数值标签位置，反转柱状图时使用
))

# 反转柱状图的x轴和y轴
bar.reversal_axis()

# 绘图
bar.render()
