def withdraw(n):
    hundreds, fifties, twenties = 0, 0, 0

    if n >= 100:
        hundreds, hundreds_remainder = divmod(n, 100)
        if hundreds_remainder % 50 != 0 or hundreds_remainder % 20 != 0:
            # remove one 100, so can split it into 50s and 20s
            hundreds -= 1
            hundreds_remainder = n - (hundreds * 100)
            n = hundreds_remainder
        else:
            n = hundreds_remainder

    if n >= 50:
        fifties, fifties_remainder = divmod(n, 50)
        if fifties_remainder % 20 != 0:
            # remove one 50
            fifties -= 1
            fifties_remainder = n - (fifties * 50)
            n = fifties_remainder
        else:
            n = fifties_remainder


    if n >= 20:
        twenties, twenties_remainder = divmod(n, 20)

    if fifties > 1:
        extra_100, final_fifties_sum = divmod(fifties*50, 100)
        hundreds += extra_100
        fifties = final_fifties_sum//50

    return [hundreds, fifties, twenties]


        
#print(withdraw(60)) # should equal [0, 0, 3]


#print(withdraw(230)) # should equal [1, 1, 4]

#print(withdraw(260))  # [2, 0, 3]

#print(withdraw(40)) # should equal [0, 0, 2]

#print(withdraw(250)) # should equal [2, 1, 0]

print(withdraw(370)) # should equal [3, 1, 1]
 
# bills are 100, 50, 20


"""
if have 230:
can split 100, 100, 30
can split 100,  50, 50, 30

230 [100, 50, 30]

230 - 100 = 130, is that div by 50 or 20? no.
so 130 - 50 = 80
"""
