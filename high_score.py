def high(x):
    x = x.split()
    sorted_words = sorted(x, key=lambda word: -sum([ord(letter) - 96 for letter in word]))
    return sorted_words[0]

