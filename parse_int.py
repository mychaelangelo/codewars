def parse_int(string):
    array_items = nums_list(string)
    item_length = len(array_items)
    print(string)
    print(array_items)


    if item_length == 0:
        return 0
    elif item_length == 1:
        return array_items[0]
    elif item_length == 2:
        return array_items[0] * array_items[1]
    elif item_length == 3:
        sum_1 = array_items[0] * array_items[1] 
        if array_items[2] not in [100,1000]:
            return sum_1 + array_items[2]
        else:
            return sum_1 * array_items[2]
    elif item_length == 4:
        if array_items[1] and array_items[3] in [100,1000]:
            sum_1 = array_items[0] * array_items[1] * array_items[3]
            sum_2 = array_items[2] * array_items[3]
            return sum_1 + sum_2
        else:
            sum_1 = array_items[0] * array_items[1] * array_items[2]
            return sum_1 + array_items[3]
        

    elif item_length == 5:
        sum_1 = array_items[0] * array_items[1]
        if array_items[2] == 1000:
            sum_1 = sum_1 * 1000
            return sum_1 + (array_items[3] * array_items[4])
        else:
            sum_2 = (array_items[2] * array_items[3]) + array_items[4]
            return sum_1 + sum_2
        
    

    elif item_length == 6:
        sum_1 = array_items[0] * array_items[1] * array_items[3]
        sum_2 = array_items[2] * array_items[3] 
        sum_3 = array_items[4] * array_items[5]
        return sum_1 + sum_2 + sum_3
    elif item_length == 7:
        sum_1 = array_items[0] * array_items[1] * array_items[3]
        sum_2 = array_items[2] * array_items[3] 
        sum_3 = array_items[4] * array_items[5]
        return sum_1 + sum_2 + sum_3 + array_items[6]


def nums_list(string):
    list_words = string.lower().split()
    list_words = [word for word in list_words if word != 'and']

    word_num = {'zero':0, 'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
                'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
                'eighteen': 18, 'nineteen': 19, 'twenty': 20,
                'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
                'seventy': 70, 'eighty': 80, 'ninety': 90,
                'hundred': 100, 'thousand': 1000, 'million': 1000000
    }
    list_of_digits = []
    for word in list_words:
        if word in word_num:
            list_of_digits.append(word_num[word])
        else:
            pair = word.split('-')
            first_part = word_num[pair[0]] // 10
            second_part = word_num[pair[1]]
            joint_str = str(first_part) + str(second_part)
            list_of_digits.append(int(joint_str))

    return list_of_digits

output = parse_int('five thousand two hundred and ten')

print(output)