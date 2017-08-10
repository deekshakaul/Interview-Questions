class node:
  def __init__(self,data=0):
    self.data=data
    self.left=None
    self.right=None
  
def identical(root,r):
  if root==None and r==None:
    return True
  elif root==None or r==None:
    return False
  elif root.data==r.data :
    return(True and identical(root.left,r.left) and identical(root.right,r.right))
  else:
    return False
    
#tree 1    
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)

#tree 2
root1=node(1)
root1.left=node(2)
root1.right=node(5)
root1.left.left=node(4)

print(identical(root,root1))
