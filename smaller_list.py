def smaller(arr):
    result = []
    for index, item in enumerate(arr):
        count = 0
        rest_of_arr = arr[index+1:]
        for comp_num in rest_of_arr:
            if comp_num < item:
                count += 1
        result.append(count)
    return result





# tests
print(smaller([5, 4, 3, 2, 1])) # Output [4, 3, 2, 1, 0]
print(smaller([1, 2, 0])) # Output [1, 1, 0]