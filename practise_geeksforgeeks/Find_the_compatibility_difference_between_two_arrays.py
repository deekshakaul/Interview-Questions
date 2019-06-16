# http://www.geeksforgeeks.org/find-compatibility-difference-two-arrays/

# O(n^2) solution
a=input().strip().split(' ')
b=input().strip().split(' ')
n=len(a)
mismatch=0
for i in range(n):
  if  a[i]==b[i]:
    pass
  else:
    j=i
    while j<b.index(a[i]):
      a[i],a[i+1]=a[i+1],a[i]
      mismatch+=1
      j+=1
print(mismatch)      
