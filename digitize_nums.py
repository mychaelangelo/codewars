def digitize(n):
    return [int(x) for x in str(n)[::-1]]


print(digitize(35231)) # should return [1,3,2,5,3]

