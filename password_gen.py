"""
requirements:
6-20 chars long
contains at least one lowercase letter >> string.ascii_lowercase
contains at least one uppercase letter >> use string.ascii_uppercase
contains at least one number >> use 'string.digits'
contains only alphanumerica chars (no special chars) 
"""

import random, string

def password_gen():
    # set length
    pass_len = random.randrange(6, 21)
    parts = {'lowers': 1, 'uppers': 1, 'nums': 1}
    len_left = pass_len - 3
    while len_left > 0:
        curr_part, curr_value = random.choice(list(parts.items()))
        parts[curr_part] = curr_value + 1
        len_left -= 1
    
    lowers_text = random.choices(string.ascii_uppercase, k=parts['lowers'])
    uppers_text = random.choices(string.ascii_lowercase, k=parts['uppers'])
    nums_text = random.choices(string.digits, k=parts['nums'])
    final_list = lowers_text + uppers_text + nums_text
    random.shuffle(final_list)
    return ''.join(final_list)
    


