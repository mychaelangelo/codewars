def binary_array_to_number(arr):
  bin_str = ''.join([str(num) for num in arr])
  return int(bin_str, 2)

#test
print(binary_array_to_number([0,1,1,0])) # should equal 6