# https://www.hackerrank.com/challenges/common-child
import sys

def commonChild(s1, s2):
    mat=[[0 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
    maxlen=0
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                mat[i][j]=mat[i-1][j-1]+1
                maxlen=max(maxlen,mat[i][j])
            else:
                mat[i][j]=max(mat[i-1][j],mat[i][j-1])

    return maxlen

        
        
    # Complete this function

s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)
