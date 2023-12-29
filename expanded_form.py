"""
psuedo code solution on n = 342
(1) convert to string '342'
(2) reverse the string i.e. reverse_string = n[::-1]
(3) each pos represents a exponent of 10, so do list comprehension into new list
(4) reverse the list
(5) create new string via join function


"""

def expanded_form(num):
    num_string = str(num)[::-1] # convert to string and reverse it
    nums_list = [int(s) for s in num_string]
    nums_list_exp = []
    pos = 0
    while pos < len(nums_list):
        curr_num = nums_list[pos]
        if curr_num != 0:
            pwd = curr_num * (10**pos)
            nums_list_exp.append(str(pwd))
        pos += 1
    nums_list_exp.reverse()
    return " + ".join(nums_list_exp)



test_input = 1023
print(expanded_form(test_input))

