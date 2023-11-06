import json
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams["font.sans-serif"] = [u"SimHei"]
plt.rcParams["axes.unicode_minus"] = False

with open('./output/地点人名.txt', mode='r') as rm:
    data = json.load(rm)

gaoben = 0
chaoben = 0
xieben = 0
keben = 0
huoziyin = 0
taoyin = 0
shiyin = 0
qianyin = 0
weifenleiyinben = 0

for i in data.values():
    for item in i:
        if '抄本' in item or '抄' in item:
            chaoben += 1
        elif '稿本' in item:
            gaoben += 1
        elif '寫本' in item:
            xieben += 1
        elif '刻本' in item or '刻' in item:
            keben += 1
        elif '活字印' in item:
            huoziyin += 1
        elif '石印' in item:
            shiyin += 1
        elif '鉛印' in item:
            qianyin += 1
        elif '印' in item:
            weifenleiyinben += 1

shouchaoben = gaoben + chaoben + xieben
yinben = keben + huoziyin + taoyin + shiyin + qianyin + weifenleiyinben

Total = shouchaoben + yinben

percentage_gaoben = (gaoben / Total) * 100
percentage_chaoben = (chaoben / Total) * 100
percentage_xieben = (xieben / Total) * 100
percentage_keben = (keben / Total) * 100
percentage_huoziyin = (huoziyin / Total) * 100
percentage_taoyin = (taoyin / Total) * 100
percentage_shiyin = (shiyin / Total) * 100
percentage_qianyin = (qianyin / Total) * 100
percentage_weifenlei = (weifenleiyinben / Total) * 100

# 数据
labels = ['稿本', '抄本', '寫本', '刻本', '活字印本', '石印本', '鉛印本', '未分類印本']
sizes = [percentage_gaoben, percentage_chaoben, percentage_xieben, percentage_keben, percentage_huoziyin,
         percentage_huoziyin, percentage_shiyin, percentage_qianyin, percentage_weifenlei]
colors = ['#FC9F4D', '#FFBA84', '#E98B2A', '#33A6B8', '#7BA23F', '#86C166', '#42602D', '#268785', '#5DAC81']


def update_pie_chart():
    selected_elements = [element.get() for element in elements]
    selected_labels = [labels[i] for i, sel in enumerate(selected_elements) if sel]
    selected_sizes = [sizes[i] for i, sel in enumerate(selected_elements) if sel]
    selected_colors = [colors[i] for i, sel in enumerate(selected_elements) if sel]

    plt.cla()  # 清除当前图形
    plt.pie(selected_sizes, labels=selected_labels, autopct='%1.1f%%', startangle=140, colors=selected_colors)  # 设置颜色
    pie_chart.set_title("Selected Elements")
    pie_chart.pie(selected_sizes, labels=selected_labels, autopct='%1.1f%%', startangle=140,
                  colors=selected_colors)  # 设置颜色
    canvas.draw()


# 创建主窗口
root = tk.Tk()
root.title("Dynamic Pie Chart")

# 创建饼图
fig, pie_chart = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# 创建元素选择框
elements = [tk.BooleanVar() for _ in labels]
element_frames = []
for i, label in enumerate(labels):
    element_frame = ttk.Frame(root)
    element_frame.pack()
    ttk.Checkbutton(element_frame, text=label, variable=elements[i], command=update_pie_chart).pack(side=tk.LEFT)
    element_frames.append(element_frame)

# 初始绘制
update_pie_chart()

root.mainloop()
