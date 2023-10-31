# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def solution(string):
    if not string:
        return string
    else:
        result = re.sub(r"(_|-)+", " ",string).title().replace(" ","")
        return ''.join([result[0].lower() if string[0].islower() else result[0], result[1:]])
    
def solution(string):
    output = ''
    capitalize = False
    for letter in string:
        if letter in {'-', '_', ' '}:
            capitalize = True
        elif capitalize:
            output += letter.upper()
            capitalize = False
        else:
            output += letter
    return output   