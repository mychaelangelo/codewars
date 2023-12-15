"""
code wars:
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
"""

# note that pin can be 1 to 8 digits

from itertools import product

def get_pins(observed):
    pin_entry = [int(item) for item in observed]
    pin_set_pairs = []
    for pin_num in pin_entry:
        pin_set_pairs.append(get_nearby(pin_num))

    pins_tuples = list(product(*pin_set_pairs))
    result = []
    for pin in pins_tuples:
        pin_str = "".join(str(num) for num in pin)
        result.append(pin_str)

    return result


def get_nearby(num):
    buttons = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [5, 7, 8, 9, 0],
        9: [6, 8, 9],
        0: [0, 8]
    }
    return buttons[num]


print(get_pins('11'))