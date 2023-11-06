import pandas as pd
import pickle
from zhconv import convert
import openpyxl
import pyecharts.options as opts
from pyecharts.charts import ThemeRiver


# 从文件中加载DataFrame
with open('./output/时间和出版方式表格.pkl', 'rb') as file:
    data = pickle.load(file)
a = data.columns.tolist()
x_data = []
for i in a:
    x_data.append(convert(i, 'zh-hans'))

y_data = []

for column in data.columns:
    for index, value in data[column].items():
        column = convert(column, 'zh-hans')
        y_data.append([index, value, column])
(
    ThemeRiver(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name=x_data,
        data=y_data,
        label_opts=opts.LabelOpts(font_size=18),
        singleaxis_opts=opts.SingleAxisOpts(
            pos_top="50", pos_bottom="50", type_="value", min_=1368, max_=1911
        ),
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
    )
    .render("./themeriver.html")
)
