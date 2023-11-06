import json


def process_strings(string, list1, list2):
    # 首先处理第一个列表
    for word in list1:
        if word in string:
            index = string.index(word)
            string = string[index + len(word):]
            break

    # 然后处理第二个列表
    for word in list2[::-1]:
        if word in string:
            index = string.rindex(word)
            string = string[:index]
            break

    return string


if __name__ == '__main__':
    with open('./output/地点人名.txt', mode='r') as rm:
        info = json.load(rm)
    determine_word = ['年', '間', '初', '末', '明', '清', '洪武', '建文', '永樂', '洪熙', '宣德', '正統', '景泰', '天順',
                      '成化', '弘治', '正德', '嘉靖', '隆慶', '萬曆', '泰昌', '天啓', '崇禎',
                      '崇德', '順治', '康熙', '雍正', '乾隆', '嘉慶',
                      '道光', '咸豐', '同治', '光緒', '宣統']
    special = ['活字印', '石印', '鉛印', '刻本', '抄本', '印本', '稿本', '寫本', '刻', '抄', '印']
    keywords = ['局', '堂', '室', '書房', '書屋', '書院', '亭', '寺', '齋', '樓', '閣', '館', '武英殿']
    for key in list(info):
        newValue = []
        filtered_list = []
        for row in info[key]:
            if len(row) != 0:
                if row[0] == '明' or row[0] == '清':
                    if process_strings(row, determine_word, special):
                        newValue.append(row[0]+process_strings(row, determine_word, special))
        for row in newValue:
            if process_strings(row, determine_word, special):
                row = row[0]+process_strings(row, determine_word, special)
        for string in newValue:
            # 檢查字符串是否包含關鍵詞列表中的任何一個關鍵詞
            if any(keyword in string for keyword in keywords):
                # 如果包含，則將該字符串添加到新列表中
                filtered_list.append(string)
        info[key] = filtered_list
        if not info[key]:
            del info[key]

    with open('./output/中间.txt', mode='w') as out:
        json.dump(info, out)
