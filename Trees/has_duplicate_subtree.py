class node:
 
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

postordersubtree=[]
def get_postorder_subtrees(tree):
  if (tree.left is None) and (tree.right is None):
    return tree.data
  temp = ""
  if tree.left is not None:
    temp = temp+ str(get_postorder_subtrees(tree.left))
  if tree.right is not None:
    temp = temp + str(get_postorder_subtrees(tree.right))
  temp = temp + str(tree.data) # Left, Right, Root
  postordersubtree.append(temp)
  return temp
  

T = node(26)
T.left=node(2)
T.left.left=node(4)
T.right=node(3)
T.right.left=node(2)
T.right.left.left=node(4)

get_postorder_subtrees(T)
print(postordersubtree)
for x in postordersubtree:
  if postordersubtree.count(x)>1:
    d=1
    
if d==1:
  print("yes")
