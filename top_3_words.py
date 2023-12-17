# exercise from code wars
import re

def top_3_words(text):
    text = text.lower() # make string all lower

    # check if any letters are in there, otherwise return empty array
    if not re.search('[a-z]', text):
        return []  

    pattern = r'\s|[^a-zA-Z\']' # split at white space or none chars
    results = re.split(pattern, text) # put into list

    word_dict = {key: results.count(key) for key in results} # put into dict
    
    if '' in word_dict: # remove blanks
        word_dict.pop('') 

    ordered_dict = list(sorted(word_dict.items(), key=lambda x: -x[1]))
    
    result_list = [x[0] for x in ordered_dict[:3]]

    return result_list

