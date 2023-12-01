"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

# Standard version
def solution(s):
    pos = 0
    result = []
    while pos < len(s):
        try:
            result.append(s[pos]+s[pos+1])
            pos += 2
        except:
            result.append(s[pos]+'_')
            break
    return result

# Recursion verison
def solution2(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s + ('_')]
    else:
        return [s[0] + s[1]] + solution2(s[2:])


print(f"Solution 1: {solution('abcde')}")
print(f"Solution 2: {solution2('abcde')}")
