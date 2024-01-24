def series_sum(n):
    if n == 0:
        return "0.00"
    denoms = list(range(1, n*3, 3))
    fracs_sum = sum([1/n for n in denoms])
    return '{:.2f}'.format(fracs_sum)

print(series_sum(1))