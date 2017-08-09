class node:
  def __init__(self,data=None):
    self.left=None
    self.right=None
    self.data=data
  
def fold(root):
  if root ==None:
    return True
  if root.left== None and root.right==None:
    return True
  if root.left == None or root.right == None:
    return False
  mirror(root.left)
  return check(root.left,root.right)
  
def mirror(root):
  if root==None:
    return
  else:
    mirror(root.left)
    mirror(root.right)
    
    temp=node()
    temp=root.right
    root.right=root.left
    root.left=temp
    
def check(r1,r2):
  if(r1== None and r2==None):
    return True
  if(r1==None or r2==None):
    return False
  return check(r1.left,r2.left) and check(r1.right,r2.right)
    
  
def inorder(root):
  if root==None:
    return
  inorder(root.left)
  root.data='1'
  inorder(root.right)
  
root = node(1)
root.left        = node(2)
root.right       = node(3)
root.left.right  = node(4)
root.right.left = node(5) 
inorder(root)
print(fold(root))



