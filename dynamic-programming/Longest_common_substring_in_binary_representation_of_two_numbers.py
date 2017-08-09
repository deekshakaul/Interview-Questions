n1,n2=list(map(int,input().strip().split(' ')))
n1=bin(n1)[2:]
print(n1)
l1=len(n1)+1
n2=bin(n2)[2:]
print(n2)
l2=len(n2)+1
lcs=[[0 for i in range(l1)]for j in range(l2)]
maxval=0
mi=0
mj=0
bin=[]
for i in range(1,l1):
  for j in range(1,l2):
    if n1[i-1]==n2[j-1]:
      lcs[i][j]=lcs[i-1][j-1]+1
for i in range(l1):
  for j in range(l2):      
    if lcs[i][j]>maxval:
      maxval=lcs[i][j]
      mi=i
      mj=j
for i in range(mi,mi-maxval,-1):
  bin.insert(0,n1[i-1])
bin=''.join(bin)
n=int(bin,2)
print(n)
