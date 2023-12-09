def high_and_low(numbers):
    nums = [int(num) for num in numbers.split()]
    return str(max(nums)) + " " + str(min(nums))

