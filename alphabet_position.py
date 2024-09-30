def alphabet_position(text):
 return ' '.join([str(ord(curr_char.lower()) - 96) for curr_char in text if curr_char.isalpha()])