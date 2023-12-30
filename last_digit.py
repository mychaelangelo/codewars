def last_digit(n1, n2):
    if n2 == 0:
        return 1
    
    patterns = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
        10: [0]
    }

    n1_last_digit = int(str(n1)[-1])

    pattern_list = patterns[n1_last_digit]
    pos_in_pattern = (n2 % len(pattern_list)) - 1

    return pattern_list[pos_in_pattern]


# tests
print(last_digit(9, 7)) # should return 9
print(last_digit(10, 10 ** 10)) # should return 0
print(last_digit(2 ** 200, 2 ** 300)) # should return 6

n1, n2 = 3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651
print(last_digit_2(n1, n2)) # should return 7