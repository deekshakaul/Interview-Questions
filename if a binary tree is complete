# to find if a binary tree is complete

class node:
  def __init__(self, data):
    self.data=data
    self.left=None
    self.right=None

# prints true if each node has either 0 or 2 children
def isComplete(root):
  if root.left!=None and root.right!=None:
    return True and isComplete(root.left) and isComplete(root.right)
  if root.left==None and root.right==None:
    return True
  if (root.left == None and  root.right!=None) or (root.left != None and  root.right==None):
    return False

# input binary tree
root=node(5)
root.left=node(2)
root.right=node(4)
root.left.left=node(5)
root.left.right=node(4)
# should print true
print(isComplete(root))

root1=node(5)
root1.left=node(2)
root1.right=node(4)
root1.left.right=node(4)
#should print false
print(isComplete(root1))
