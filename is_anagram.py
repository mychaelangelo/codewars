def is_anagram(test, original):
    test, original = test.lower(), original.lower()
    if len(test) != len(original):
        return False
    for letter in test:
        if letter not in original:
            return False
    return True
        
