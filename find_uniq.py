def find_uniq(arr):
    mid_point = len(arr) // 2
    arr_1 = arr[:mid_point]
    arr_2 = arr[mid_point:]
    if sum(arr_1) / len(arr_1) == arr_1[0]:
        same = arr_1[0]
    else:
        same = arr_2[0]
    
    for num in arr:
        if num != same:
            return num



