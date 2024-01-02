def alphabet_position(text):
    text = text.lower()
    return ' '.join([str(ord(item)-96) for item in text if item.isalpha()])

print(alphabet_position("The sunset sets at twelve o' clock."))