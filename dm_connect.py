# -*- coding = utf-8 -*-
# @Time : 2020/10/8 10:57
# @Author : 周芳
# @File : dm_connect.py
# @Software:PyCharm

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.commons.utils import JsCode
x_data=['2019-1','2019-2','2020-1','2020-2']
v1 = [42758.41, 101616.1,,35916.58,100840.11]
v2 = [1379.3, 3277.94, 5240.88,  8014.38,  1158.6, 3252.91]
v3 = [0.198,0.222,0.175,0.222]

bar = (
    Bar()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis("建筑行业总产值",v1)
    .add_yaxis("季度内生产总值",v2)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value}"),interval=0.05
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Overlap-bar+line"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 亿元")),
    )
)
line = Line().add_xaxis(xaxis_data=x_data).add_yaxis("比例",v3, yaxis_index=1)
bar.overlap(line)
bar.render("overlap_bar_line.html")