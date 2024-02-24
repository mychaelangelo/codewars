def first_non_consecutive(arr):
    pos = 1
    while pos < len(arr):
        if arr[pos] != arr[pos-1] + 1:
            return arr[pos]
        pos += 1
    return None

print(first_non_consecutive([1,2,3,4,6,7,8]))