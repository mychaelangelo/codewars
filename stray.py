def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num

print(stray([1, 1, 1, 1, 1, 1, 2])) # should equal 2