def number(lines):
    return [f"{index+1}: {item}" for index, item in enumerate(lines)]

    
print(number(["a","b"]))