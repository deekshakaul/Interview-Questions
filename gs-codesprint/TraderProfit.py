#!/bin/python3
import sys

def traderProfit(k, n, A):
  #T stores the details of max profit
    T=[[0 for i in range(n)]for j in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,n):
          for m in range(0,j):
            T[i][j]=max(T[i][j],T[i][j-1],T[i-1][m]+A[j]-A[m])
    return T[-1][-1]
  
q = int(input().strip())
for a0 in range(q):
    k = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = traderProfit(k, n, arr)
    print(result)
