def find_it(seq):
    item_counts = {num: seq.count(num) for num in seq if seq.count(num) % 2 != 0}
    return list(item_counts)[0]
    

print(find_it([1,2,3,3,4]))