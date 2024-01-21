def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        output = numbers.copy()
        output.remove(min(output))
        return output
    
"""
learnt something new here. you can't just do copy_list = old_list,
since copy_list would just be a pointer to the original list, and you'd still
be modifying the old list. So you have to do copy_list = old_list.copy().

you can also do copy_list = list(old_list)

see: https://www.w3schools.com/python/python_lists_copy.asp

"""