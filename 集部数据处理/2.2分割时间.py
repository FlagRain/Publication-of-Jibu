import re
import json


def time_mining(s):
    era_names = ['洪武', '建文', '永樂', '洪熙', '宣德', '正統', '景泰', '天順',
                 '成化', '弘治', '正德', '嘉靖', '隆慶', '萬曆', '泰昌', '天啓', '崇禎',
                 '崇德', '順治', '康熙', '雍正', '乾隆', '嘉慶',
                 '道光', '咸豐', '同治', '光緒', '宣統']
    dynasty_name = ['明', '清']
    determine_word = ['年', '間', '初', '末']

    matches = []
    for dynasty in dynasty_name:
        for i in determine_word:
            pattern = re.escape(dynasty) + r'(.*?)' + re.escape(i)
            match = re.search(pattern, s)
            if match:
                res = match.group(0)
                matches.append(res)
    for era in era_names:
        if '明' not in s and '清' not in s and era in s:
            matches.append(era)
            break
    if len(matches):
        shortest = matches[0]
        for string in matches:
            if len(string) < len(shortest):
                shortest = string
        return shortest


if __name__ == '__main__':

    with open('./output/地点人名.txt', mode='r', encoding='utf-8') as raw:
        info = json.load(raw)
        for key in list(info):
            newValue = []
            for row in info[key]:
                if time_mining(row):
                    newValue.append(time_mining(row))
            info[key] = newValue
            if not info[key]:
                del info[key]

    with open('./output/time_info.txt', mode='w', encoding='utf-8') as out:
        json.dump(info, out)
    