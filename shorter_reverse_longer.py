def shorter_reverse_longer(a,b):
    shorter, longer = a if len(a) < len(b) else b, a if len(b) <= len(a) else b
    return shorter+longer[::-1]+shorter


print(shorter_reverse_longer("first", "abcde")) # should return "abcdetsrifabcde"