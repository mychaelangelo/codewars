def solution(s):
    if s:
        result = s[0] +  ""
        for letter in s[1:]:
            if letter.isupper():
                result += " " + letter
            else:
                result += letter
        return result
    else:
        return s


print(solution("breakCamelCase"))