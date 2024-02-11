def nb_dig(n, d):
    nums = [x**2 for x in range(n+1)]
    count = 0
    for num in nums:
        if str(num).count(str(d)) > 0:
            count+=str(num).count(str(d))
    return count


#print(nb_dig(10, 1)) #should return 4
print(nb_dig(8304, 7)) #should equal 3927