def abbrev_name(name):
    names = name.split()
    first, last = names[0][0].upper(), names[1][0].upper()    
    return f"{first}.{last}"

print(abbrev_name("Sam Harris"))