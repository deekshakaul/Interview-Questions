# https://www.hackerrank.com/challenges/string-reduction/problem
from collections import Counter
test=int(input().strip())
for t in range(test):
    s=input().strip()
    if len(Counter(s))==1:
        print(len(s))
    elif (s.count('a')%2==0  and s.count('b')%2==0 and s.count('c')%2==0) or (s.count('a')%2==1 and s.count('b')%2==1 and s.count('c')%2==1) :
        print(2)
    else:
        print(1)
