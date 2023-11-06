import json
import matplotlib.pyplot as plt
import re
import pandas as pd
import pickle
import openpyxl


with open('./output/地点人名.txt', mode='r') as rm:
    data = json.load(rm)

era_names = ['洪武', '建文', '永樂', '洪熙', '宣德', '正統', '景泰', '天順',
             '成化', '弘治', '正德', '嘉靖', '隆慶', '萬曆', '泰昌', '天啓', '崇禎',
             '崇德', '順治', '康熙', '雍正', '乾隆', '嘉慶',
             '道光', '咸豐', '同治', '光緒', '宣統']

with open('年号词典.txt', mode='r') as nianhao:
    era_names_dict = json.load(nianhao)

year_list = []
for i in era_names_dict.values():
    year_list.append(int(i[:-1]))

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
    dict_with_value = {}.fromkeys(year_list, 0)
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
    return dict_with_value


if __name__ == '__main__':
    row_index = year_list
    column_index = ['稿本', '抄本', '寫本', '刻本', '活字印本', '石印本', '鉛印本', '未分類印本']
    df = pd.DataFrame(0, index=row_index, columns=column_index)
    for i in data.values():
        for item in i:
            if '抄' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '抄本'] += value
            elif '刻' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '刻本'] += value
            elif '稿本' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '稿本'] += value
            elif '寫本' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '寫本'] += value
            elif '活字印' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '活字印本'] += value
            elif '石印' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '石印本'] += value
            elif '鉛印' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '鉛印本'] += value
            elif '印' in item:
                for year, value in time_transform(item).items():
                    if value != 0:
                        df.loc[year, '未分類印本'] += value
    with open('./output/时间和出版方式表格.pkl', 'wb') as file:
        pickle.dump(df, file)
