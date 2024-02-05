def remove_every_other(my_list):
    res = []
    for index, item in enumerate(my_list):
        if index % 2 == 0: # if is even
            res.append(item)
    return res

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))