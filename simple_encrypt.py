
def encrypt(text, n):
    if text is None:
        return None
    if text == "" or n <= 0:
        return text
    if n == 1:
        odds = ''.join([item for index, item in enumerate(text) if index % 2 != 0])
        evens = ''.join([item for index, item in enumerate(text) if index % 2 == 0])
        return odds + evens
    else:
        odds = ''.join([item for index, item in enumerate(text) if index % 2 != 0])
        evens = ''.join([item for index, item in enumerate(text) if index % 2 == 0])
        n -= 1
        return encrypt(odds+evens, n)


def decrypt(encrypted_text, n):
    if encrypted_text == '' or n < 0:
        return encrypted_text
    if encrypted_text is None:
        return None
    
    count = 0
    while count < n:
        result = ""
        odd_len = len(encrypted_text) // 2
        odds = encrypted_text[:odd_len]
        evens = encrypted_text[odd_len:]

        for even_item in evens:
            if odds:
                pair_b = odds[0]
                odds = odds[1:]
                pair = even_item + pair_b
            else:
                pair = even_item
            result += pair
        count += 1
        encrypted_text = result
    return encrypted_text



print(encrypt(None, 1))
