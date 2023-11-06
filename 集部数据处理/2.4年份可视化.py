import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import json

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
    with open('./output/time_info.txt', mode='r') as raw:
        timeDict = json.load(raw)
    for values in timeDict.values():
        for i in values:
            time_transform(i)
    print(dict_with_value)
    with open('../aaa.txt', mode='w') as f2:
        json.dump(dict_with_value, f2)
    df = pd.DataFrame(list(dict_with_value.items()), columns=['Year', 'Count'])

    fig = px.line(df, x='Year', y='Count')
   # fig.show()
