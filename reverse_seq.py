def reverse_seq(n):
   result = [num for num in range(1, n+1)]
   result.reverse()
   return result


print(reverse_seq(5))