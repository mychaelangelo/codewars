def count_bits(n):
    return bin(n).count('1')

print(count_bits(7)) # should equal 3