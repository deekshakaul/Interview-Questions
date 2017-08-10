class node:
  def __init__(self,data=0):
    self.data=data
    self.left=None
    self.right=None
  
def size(root):
  if root==None:
    return 0
  else:
    return size(root.left)+1+size(root.right)
    
#tree   
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.left.right.left=node(6)

print(size(root))
