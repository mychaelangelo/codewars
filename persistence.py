#exercise from codewars

import math
def persistence(n):
    list_of_nums = [int(n) for n in str(n)]
    count = 0
    while len(list_of_nums) > 1:
        prod = math.prod(list_of_nums)
        list_of_nums = [int(n) for n in str(prod)]
        count += 1
    return count
