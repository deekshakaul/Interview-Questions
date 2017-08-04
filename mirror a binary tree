class node:
  def __init__(self,data=0):
    self.data=data
    self.left=None
    self.right=None

#recursively call mirror for left and right subtrees and swap subtrees 
def mirror(root):
  if root == None:
    return 
  else:
    mirror(root.right)
    mirror(root.left)
    root.left,root.right=root.right,root.left
  
#print preorder traversal of tree
def preorder(root):
  if root==None:
    return 
  else:
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)
  
r=node(1)  
r.left=node(2)
r.right=node(3)
r.left.left=node(4)
r.left.right=node(5)
r.right.left=node(6)
r.right.right=node(7)
preorder(r)	#tree before mirror
mirror(r)
print()
preorder(r)	#tree after mirror
