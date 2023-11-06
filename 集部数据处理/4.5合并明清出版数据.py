import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel('ming.xlsx')

# 读取第二个Excel文件
df2 = pd.read_excel('qing.xlsx')
print(df1)
# 合并两个数据框，按第一列文本进行合并，并对第二列数据相加
merged_df = df1.merge(df2, on='列1', how='outer')
merged_df['列2_x'].fillna(0, inplace=True)  # 将NaN值替换为0
merged_df['列2_y'].fillna(0, inplace=True)  # 将NaN值替换为0
merged_df['列2'] = merged_df['列2_x'] + merged_df['列2_y']  # 相加第二列数据
merged_df = merged_df[['列1', '列2']]  # 选择需要的列

# 保存结果到一个新的Excel文件
merged_df.to_excel('合并后的文件.xlsx', index=False)