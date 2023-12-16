import time

cache = {}

def fibonacci(n):
    if n in [0, 1]:
        return n
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

