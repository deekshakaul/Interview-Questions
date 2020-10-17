#https://leetcode.com/problems/string-to-integer-atoi/

import re

def myAtoi(str: str) -> int:
    numStr = list(str.strip(' '))
    isNegative = False
    number = 0
    if len(numStr) == 0:
        return 0
    if numStr[0] == '-':
        numStr.pop(0)
        isNegative = True
    elif numStr[0] == '+':
        numStr.pop(0)
    for i in numStr:
        if i.isdigit():
            number = number * 10 + int(i)
        else:
            break
    if not (number > -2147483649 and number < 2147483648):
        if isNegative:
            return -2147483648
        else:
            return 2147483647
    if isNegative:
        return number * -1
    else:
        return number

string = input().strip()
result = myAtoi(string)
print(result)
