def find_short(s):
    s_words = s.split()
    return min([len(x) for x in s_words])


print(find_short("Lets all go on holiday somewhere very cold"))