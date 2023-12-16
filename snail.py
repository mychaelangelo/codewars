# 3 hours to solve.

def snail(snail_map):
    if len(snail_map) == 1:
        return snail_map[0]
    if len(snail_map) == 2:
        snail_map[1].reverse()
        return snail_map[0] + snail_map[1]
    else:
        top_block = snail_map.pop(0) # get the top block
        snail_map[-1].reverse()
        bottom_block = snail_map.pop(-1) # get the bottom block

        right_block = []
        for row in snail_map:
            right_block.append(row.pop(-1))
        left_block = []
        for row in snail_map:
            left_block.append(row.pop(0))
        left_block.reverse()
        
        return top_block + right_block + bottom_block + left_block + snail(snail_map)









my_array = [[1,2],
            [3,4]]

my_array1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]

my_array2 = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]

print(snail(my_array))
