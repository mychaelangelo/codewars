# from codewars.com
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

def rgb(r, g, b):
    hex_val = ""
    for item in [r, g, b]:
        hex_val += num_to_hex(item)
    return hex_val

def num_to_hex(num):
    if num < 0:
        num = 0
    elif num > 255:
        num = 255
    hex_map = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    wholes = num // 16
    parts = num % 16
    if wholes > 9:
        wholes = hex_map[wholes]
    if parts > 9:
        parts = hex_map[parts]
    return str(wholes) + str(parts)



result = rgb(254, 253, 252)
print(result)