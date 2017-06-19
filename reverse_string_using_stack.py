

def createStack():
  stack=[]
  return stack
  
def stackSize(stack):
  return len(stack) 

def isempty(x):
  if stackSize(x)==0:
    return True
  else: return False
    
def push(stack,ch):
  stack.append(ch)

def pop(stack):
  output=""
  while isempty(stack)==False:
    output=output+stack.pop()
  return output
    
x=input().strip()
stack=createStack()
for i in x:
  push(stack,i)
print(pop(stack))
  
    
    
