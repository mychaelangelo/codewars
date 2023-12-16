def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    if string[0].isupper():
        string = string[0].lower() + string[1:]
    result = [ "_" + s.lower() if s.isupper() and string.index(s) != 0 else s for s in string  ]
    return "".join(result)






my_string = "App7Test"
print(to_underscore(my_string))
