def square_digits(num):
    result = ''
    for curr_num in str(num):
        result += str(int(curr_num)*int(curr_num))
    return int(result)

print(square_digits(0))