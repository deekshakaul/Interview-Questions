mi=-4294967296
ma=4294967296
class node:
  def __init__(self,data=None):
    self.left=None
    self.right=None
    self.data=data
    
def check(root, Min,Max):
  if root==None:
    return True
  if root!=None:
    if root.data<Min or root.data>Max:
      return False
    return check(root.left,Min,root.data-1) and check(root.right,root.data+1,Max)
  
def bst(root):
  if root!=None:
    return check(root,mi,ma)

root = node(1)
root.left        = node(2)
root.right       = node(3)
root.left.left  = node(4)
root.left.right = node(5) 
a=bst(root)
print(a)
r1=node(5)
r1.left=node(2)
r1.left.right=node(3)
a=bst(r1)
print(a)

