import wordcloud
import docx


def read_doc(filename):
    doc = docx.Document(filename)  # 打开Word文档
    text = []

    for paragraph in doc.paragraphs:
        text.extend(paragraph.text.split())  # 分割文本并添加到列表

    return text


if __name__ == '__main__':
    with open('./rm/书坊统计关键词-纯净版.docx', mode='rb') as f1:
        names = read_doc(f1)
    words = []
    for name in names:
        for item in name:
            words.append(item)
    string = ' '.join(words)

    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path='msyh.ttc',
                            collocations=False
                            )
    w.generate(string)

    w.to_file('shufang.png')