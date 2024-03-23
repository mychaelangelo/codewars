def gimme(input_array):
    # Implement this function
    sorted_copy = input_array.copy()
    sorted_copy.sort()
    mid_num = sorted_copy[1]
    return input_array.index(mid_num)


print(gimme([5, 10, 14]))