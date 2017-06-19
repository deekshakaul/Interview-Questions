class node:

    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def toSum(root):
  if root == None:
    return 0
  x=root.data
  root.data=toSum(root.left) + toSum(root.right)
  return root.data+x
  
def inorder(root):
  if root==None:
    return
  inorder(root.left)
  print(root.data,end=" ")
  inorder(root.right)
 
root = node(10);
root.left = node(-2);
root.right = node(6);
root.left.left = node(8);
root.left.right = node(-4);
root.right.left = node(7);
root.right.right = node(5);
inorder(root)
print('\n')
toSum(root)
inorder(root)
