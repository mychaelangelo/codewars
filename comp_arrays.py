def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    for item in array1:
        if item*item in array2:
            array2.remove(item*item)

    return len(array2) == 0

