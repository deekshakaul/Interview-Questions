class node:
  def __init__(self,data=None):
    self.left=None
    self.right=None
    self.data=data
  
def dub(root):
  if root==None:
    return
  dub(root.left)
  dub(root.right)
  temp=root.left
  root.left=node(root.data)
  root.left.left=temp
  
def inorder(root):
  if root==None:
    return
  inorder(root.left)
  print(root.data)
  inorder(root.right)
  
root = node(1)
root.left        = node(2)
root.right       = node(3)
root.left.left  = node(4)
root.left.right = node(5) 
inorder(root)
print("##############")
dub(root)
inorder(root)
