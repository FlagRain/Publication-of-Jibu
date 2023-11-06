import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt
import json
import re
import numpy as np

plt.rcParams["font.sans-serif"] = [u"SimHei"]
plt.rcParams["axes.unicode_minus"] = False

era_names = ['洪武', '建文', '永樂', '洪熙', '宣德', '正統', '景泰', '天順',
             '成化', '弘治', '正德', '嘉靖', '隆慶', '萬曆', '泰昌', '天啓', '崇禎',
             '崇德', '順治', '康熙', '雍正', '乾隆', '嘉慶',
             '道光', '咸豐', '同治', '光緒', '宣統']

with open('年号词典.txt', mode='r') as nianhao:
    era_names_dict = json.load(nianhao)

year_list = []
for i in era_names_dict.values():
    year_list.append(int(i[:-1]))
year_list = list(set(year_list))
years = list(range(1368, 1912, 16))
year_ranges = [f"{start}-{start+16}" for start in years]
df = pd.DataFrame(year_ranges, columns=['Years'])

folder_path = './output/别集总集分类'
file_path = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path.append(os.path.join(root, file))

for name in file_path:
    dict_with_value = {}.fromkeys(year_list, 0)
    years = {}.fromkeys(era_names, 0)
    for s in era_names:
        for i in list(era_names_dict):
            if s in i:
                years[s] += 1


    def time_transform(s):
        """
        处理时间并输入一个词典
        :param s:
        :return:
        """
        # 判断是否是年号
        for name, year in era_names_dict.items():
            if name in s:
                dict_with_value[int(year[:-1])] += 1
                break
        else:
            for name, year in era_names_dict.items():
                if name[:2] in s:
                    for i in era_names_dict:
                        if i[:2] == name[:2]:
                            dict_with_value[int(era_names_dict[i][:-1])] += 1 / years[name[:2]]
                    break
            else:
                if '明初' in s:
                    for i in era_names_dict:
                        if i[:2] == '洪武':
                            dict_with_value[int(era_names_dict[i][:-1])] += 1 / years['洪武']
                elif '明末' in s:
                    for i in range(1621, 1645):
                        dict_with_value[i] += 1/24
                elif '清初' in s:
                    for i in range(1645, 1680):
                        dict_with_value[i] += 1 / 35
                elif '清末' in s:
                    for i in range(1840, 1912):
                        dict_with_value[i] += 1/72


    if __name__ == '__main__':
        with open(name, mode='r') as raw:
            timeDict = json.load(raw)
        for values in timeDict.values():
            for i in values:
                time_transform(i)
        pattern = r'[^\/\\]+\.(\w+)$'
        # 查找匹配的文件名
        match = re.search(r'[^\\]*$', name).group(0)
        match = match[:-4]
        sum_data = []

        new_dict = {}
        current_year = 1368  # 设置起始年份
        end_year = 1911  # 设置结束年份

        while current_year <= end_year:
            interval_sum = 0
            for year in range(current_year, current_year + 16):
                if year in dict_with_value:
                    interval_sum += dict_with_value[year]

            new_dict[current_year] = interval_sum
            current_year += 16
        df.loc[:, match] = list(new_dict.values())

column_names = df.columns.tolist()[1:]
fig = px.line(df, x='Years', y=column_names)
fig.show()
