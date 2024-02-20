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

