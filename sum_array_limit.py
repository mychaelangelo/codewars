def sum_array(arr):
    if arr is None or len(arr) == 1:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])

print(sum_array([6, 2, 1, 8, 10]))