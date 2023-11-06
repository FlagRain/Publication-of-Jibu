import docx
import re


def segmentation(input_list):
    result = []
    sub_list = []
    input_list = [item for item in input_list if re.search(r'[\u4e00-\u9fff]', item)]
    input_list = [item for item in input_list if '中國古籍總目' not in item]
    input_list = [item for item in input_list if '之屬' not in item]
    input_list = [item for item in input_list if '集類' not in item]

    for item in input_list:
        if item[1:-1].isdigit():  # 检查元素是否为编号
            if sub_list:  # 如果子列表不为空，将其添加到结果列表中
                result.append(sub_list)
            sub_list = [item]  # 创建一个新的子列表，以当前编号元素为开始
        else:
            sub_list.append(item)  # 非编号元素添加到当前子列表中

    if sub_list:  # 处理最后一个子列表
        result.append(sub_list)

    return result


def read_doc(filename):
    doc = docx.Document(filename)  # 打开Word文档
    text = []

    for paragraph in doc.paragraphs:
        text.extend(paragraph.text.split())  # 分割文本并添加到列表

    return text


with open('./rm/All.docx', mode='rb') as filename:
    word_text_list = read_doc(filename)

out = segmentation(word_text_list)


with open('./output/全部.txt', mode='w', encoding='utf-8') as f1:
    for i in out:
        f1.write('\n'.join(i))
        f1.write('\n\n')
