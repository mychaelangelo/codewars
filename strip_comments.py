"""
Complete the solution so that it strips all text that follows any of a set of 
comment markers passed in. Any whitespace at the end of the line should also 
be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas

Code would be called as follows:
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

"""
import re

import re

def strip_comments(strng, markers):
    for marker in markers:
        escaped_marker = re.escape(marker)
        pattern = rf'{escaped_marker}.*?(?=$|\n)'
        strng = re.sub(pattern, '', strng)
    strng = re.sub(r'[ \t]+$', '', strng, flags=re.MULTILINE)
    return strng

input_string = "apples, pears # and bananas\ngrapes\nbananas !apples"
marks_to_use = ["#", "!"]
result = strip_comments(input_string, marks_to_use)
print(f"input is: {input_string}.")
print(f"\nResult is: {result}.")
print()
print(repr(result))