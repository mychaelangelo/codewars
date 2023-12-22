#code wars kata 6kyu
import string

def is_pangram(s):
    s_list = list(s.lower()) # convert to all lower case
    s_list = list(set(s_list)) # remove duplicates by using set function
    matches = [letter for letter in string.ascii_lowercase if letter in s_list]
    return len(matches) == 26



sentence = "The quick brown fox jumps over the lazy dog"
#sentence = "1bcdefghijklmnopqrstuvwxyz"
print(is_pangram(sentence))