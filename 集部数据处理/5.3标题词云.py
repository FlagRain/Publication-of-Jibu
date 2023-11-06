import jieba
import json
import wordcloud
from pyecharts import WordCloud


with open('./output/标题.txt', mode='r') as f1:
    rm = json.load(f1)

seg_list = []
for i in rm.values():
    seg_list.extend(jieba.lcut(str(i), cut_all=True))
ls = [word for word in seg_list if len(word)==1]
element_count = {}
for item in ls:
    if item in element_count:
        element_count[item] += 1
    else:
        element_count[item] = 1

string = ' '.join(ls)
wc = WordCloud()
wc.add("",element_count.keys(),element_count.values(), #字典d = {key1 : value1, key2 : value2 }
       word_size_range=[20, 100], #单词字体大小
       )
wc.render("aaa.html")
'''
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        collocations=False
                        )
w.generate(string)

w.to_file('biaoti.png')
'''