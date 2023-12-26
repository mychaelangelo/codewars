def get_sum(a,b):
    if a == b:
        return a
    a, b = min(a,b), max(a,b)
    return sum(list(range(a, b+1)))