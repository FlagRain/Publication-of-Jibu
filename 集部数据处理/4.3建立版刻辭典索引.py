import docx
import json

dic = {}


def read_doc(filename):
    doc = docx.Document(filename)  # 打开Word文档
    text = []
    for paragraph in doc.paragraphs:
        text.extend(paragraph.text.split())  # 分割文本并添加到列表
    return text


if __name__ == '__main__':
    with open('./rm/新建 Microsoft Word 文档.docx', mode='rb') as f1:
        rm = read_doc(f1)
    indices = [index for index, word in enumerate(rm) if '［' in word or '］' in word]
    for i in range(len(indices)):
        if indices[i] != indices[-1]:
            key = rm[indices[i]][1:-1]
            value = ''
            for k in range(indices[i]+1, indices[i+1]):
                value += rm[k]
            dic[key] = value
        else:
            key = rm[indices[i]][1:-1]
            value = ''
            for k in range(indices[i] + 1, len(rm)):
                value += rm[k]
            dic[key] = value

    with open('./output/版刻索引.txt', mode='w') as out:
        json.dump(dic, out)
