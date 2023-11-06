import re
import json


def remove_after_keyword(text, keyword):
    pattern = f"{re.escape(keyword)}.*"  # 匹配关键词后的任何字符
    result = re.sub(pattern, keyword, text)  # 用关键词替换匹配的部分
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
    special = ['刻本', '抄本', '印本', '稿本', '寫本']
    special2 = ['刻', '抄', '印']
    for i in out:
        res[i[0]] = []
        for item in i:
            for spe in special:
                if spe in item:
                    res[i[0]].append(remove_after_keyword(item, spe))
                    break
            else:
                for spe2 in special2:
                    if spe2 in item:
                        index = item.find('（')
                        result_string = item[index + 1:]
                        res[i[0]].append(remove_after_keyword(result_string, spe2))
                        break

    for key in list(res):
        if not res[key]:
            del res[key]

    with open('./output/地点人名.txt', mode='w', encoding='utf-8') as f1:
        json.dump(res, f1)
