def points(games):
    x_final = 0
    for pair in games:
        score_x = pair[0]
        score_y = pair[-1]
        if score_x > score_y:
            x_final += 3
        if score_x == score_y:
            x_final +=1
    return x_final
