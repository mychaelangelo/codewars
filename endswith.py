# Function that returns true, if the first string ends with the second bit
"""
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""

def solution(text, ending):
    return text[-len(ending):] == ending

"""
Lesson: You can also just use string method, 'endswith()'
https://www.w3schools.com/python/ref_string_endswith.asp
"""