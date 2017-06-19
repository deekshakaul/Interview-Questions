#To reverse a string

output=[]

def stringReverse(str):
  x=""
  #check every charecter in string
  for i in str:
    output.append(i)
  while len(output)>0:
    a=output.pop()
    x=x+a
  return x
    
x=input()
t=stringReverse(x)
print("reversed string is: "+t)
