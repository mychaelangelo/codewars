def xo(s):
    s = s.lower()
    if 'x' and 'o' not in s:
        return True
    else:
        return s.count('x') == s.count('o')
    
print(xo('XH'))