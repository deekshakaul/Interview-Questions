output=[]
def evaluatePostfix(str):
  #check every charecter in string
  for i in str:
    if i.isdigit():
      #if not an operand append to output string
      output.append(int(i))
    #if not a digit pop two elements and perform operation
    elif i == '+':
      b=output.pop()
      c=output.pop()
      output.append(int(b+c))
    elif i == '-':
      b=output.pop()
      c=output.pop()
      output.append(int(c-b))
    elif i == '*':
      b=output.pop()
      c=output.pop()
      output.append(int(b*c))
    elif i == '/':
      b=output.pop()
      c=output.pop()
      output.append(int(c/b))
    elif i == '%':
      b=output.pop()
      c=output.pop()
      output.append(int(c%b))
x=input()
evaluatePostfix(x)
#after evaluation only one element left in the output array
print(output[0])
  
