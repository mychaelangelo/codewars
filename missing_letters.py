def find_missing_letter(chars):
    curr = ord(chars[0])
    for letter in chars[1:]:
        if ord(letter) != (curr + 1):
            return chr(ord(letter)-1)    
        curr = ord(letter)
        print(curr)


print(find_missing_letter(['a','b','c','d','f'])) # should be 'e'