import re
import json


def remove_after_keyword(text, keyword):
    pattern = f"{re.escape(keyword)}.*"  # 匹配关键词后的任何字符
    result = re.sub(pattern, '', text)  # 用关键词替换匹配的部分
    return result


if __name__ == '__main__':
    out = []  # 用于存储子列表的列表
    current_sublist = []  # 用于存储当前子列表的列表

    # 打开文本文件进行读取
    with open('./output/全部.txt', mode='r', encoding='utf-8') as rm:
        for line in rm:
            line = line.strip()  # 去除行末的换行符和空格

            if line:  # 如果不是空行，将其添加到当前子列表
                current_sublist.append(line)
            else:  # 如果是空行，开始一个新的子列表
                if current_sublist:  # 确保当前子列表不为空
                    out.append(current_sublist)
                    current_sublist = []  # 重置当前子列表
    # 处理文件末尾可能的子列表
    if current_sublist:
        out.append(current_sublist)

    res = {}
    for entry in out:
        if len(entry) > 1:
            for index, i in enumerate(entry):
                if '卷' in i:
                    res[entry[0]] = entry[1]
                    if index > 1:
                        for num in range(index)[:-1]:
                            res[entry[0]] += entry[num+2]
                    break
    keywords = ['口', '不分卷', '卷', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '洪武', '建文',
                '永樂', '洪熙', '宣德', '正統', '景泰', '天順',
                '成化', '弘治', '正德', '嘉靖', '隆慶', '萬曆', '泰昌', '天啓', '崇禎',
                '崇德', '順治', '康熙', '雍正', '乾隆', '嘉慶',
                '道光', '咸豐', '同治', '光緒', '宣統']
    for key, value in list(res.items()):
        for keyword in keywords:
            res[key] = remove_after_keyword(res[key], keyword)

    with open('./output/标题.txt', mode='w') as f1:
        json.dump(res, f1)
