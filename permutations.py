from itertools import permutations as perm

def permutations(s):
    output_perms = perm(list(s))
    list_output = list(set([''.join(list(i)) for i in output_perms]))
    return list_output

output = permutations('aabb')
print(output)
