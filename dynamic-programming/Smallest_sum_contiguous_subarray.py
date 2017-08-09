a=list(map(int,input().strip().split(' ')))
res=a
for i in range(1,len(a)):
  res[i]=min(a[i],a[i]+res[i-1])
print(min(res))
