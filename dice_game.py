def score(dice):
    score = 0
    uniques = dict.fromkeys(dice)
    for key in uniques:
        uniques[key] = dice.count(key)
    print(uniques)
    for k, v in uniques.items():
        if k == 1:
            if v >= 3:
                score += 1000 + (100 * (v-3))
            else:
                score += (100 * v)
        if k == 2 and v >= 3:
            score += 200 
        if k == 3 and v >= 3:
            score += 300 
        if k == 4 and v >= 3:
            score += 400 
        if k == 5:
            if v >= 3:
                score += 500 + (50 * (v-3))
            else:
                score += (50 * v)
        if k == 6 and v >= 3:
            score += 600
    return score



result = score([5, 1, 3, 4, 1])
print(result)