def is_uppercase(inp):
    for item in inp:
        if item.islower():
            return False
    return True