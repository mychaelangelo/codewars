
def tower_builder(n_floors):
    output_list = []
    curr_level = 1
    spaces = n_floors - 1
    star_num = 1
    while curr_level <= n_floors:
        stars = (" " * spaces) + ("*" * star_num) + (" " * spaces)
        output_list.append(stars)
        curr_level += 1
        spaces -= 1
        star_num += 2
    return output_list
        


height = 3
print(tower_builder(height))