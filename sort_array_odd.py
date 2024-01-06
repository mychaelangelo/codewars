def sort_array(source_array):
    odds_list = [item for item in source_array if item % 2 != 0]
    odds_list.sort()

    for pos, item in enumerate(source_array):
        if item % 2 != 0:
            source_array[pos] = odds_list.pop(0)            

    return source_array


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))