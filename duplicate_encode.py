def duplicate_encode(word):
    s = ""
    word = word.lower()
    for letter in word:
        if word.count(letter) == 1:
            s += "("
        if word.count(letter) > 1:
            s += ")"
    return s

print(duplicate_encode('(( @'))