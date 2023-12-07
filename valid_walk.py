def is_valid_walk(walk):
    #determine if walk is valid
    pos_x, pos_y = 0, 0
    for step in walk:
        if step == 'n':
            pos_y += 1
        elif step == 's':
            pos_y -= 1
        elif step == 'e':
            pos_x += 1
        elif step == 'w':
            pos_x -= 1
    return pos_x == 0 and pos_y == 0 and len(walk) == 10

walk_entry = ['n','s','n','s','n','s','n','s','n']
print(is_valid_walk(walk_entry))