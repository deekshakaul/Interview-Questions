# https://www.hackerrank.com/challenges/sherlock-and-valid-string
import sys
from collections import Counter 

def isValid(s):
    counts=Counter(s)
    Temp=counts.values()
    countC=Counter(Temp)
    if len(countC)==1:
        return 'YES'
    elif len((countC))>2:
        return 'NO'
    elif len(countC)==2 and min(countC.values())==1:
        return 'YES'
    else:
        return 'NO'
    

s = input().strip()
result = isValid(s)
print(result)
