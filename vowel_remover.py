def shortcut(s):
    vowels = ['a','e','i','o','u']
    new_s = ''.join([letter for letter in s if letter not in vowels])
    return new_s


# test
print(shortcut("codewars"))