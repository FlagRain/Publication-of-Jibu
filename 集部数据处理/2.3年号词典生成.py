import pandas as pd
import json

# 读取Excel文件
with open(r'C:\Users\flagr\Desktop\杜甫出版\年号查询.xlsx', mode='rb') as ninhao:
    df = pd.read_excel(ninhao)

# 创建一个空字典
my_dict = {}

# 遍历DataFrame的行
for index, row in df.iterrows():
    key = row[1]  # 第二列作为键
    value = row[0]  # 第一列作为值
    my_dict[key] = value

with open('年号词典.txt', mode='w') as out:
    json.dump(my_dict, out)
