str=list(input().strip())
count=0
stack=[]
for i in str:
  if len(stack)==0:
    stack.append(i)
  elif stack[-1]!=i:
    stack.append(i)
  else:
    count+=1
print(count)    
