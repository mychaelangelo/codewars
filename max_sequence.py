def max_sequence(arr):
    if len(arr) == 0 or all(item < 0 for item in arr):
        return 0
    curr_sum = arr[0]
    max_sum = arr[0]

    for item in arr[1:]:
        curr_sum = max(item, curr_sum + item)
        max_sum = max(curr_sum, max_sum)
        
    return max_sum
    


# tests
items = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(items)) # should result sum 6 for list [4, −1, 2, 1]