class node :
  def __init__(self,data):
    self.left=None
    self.right=None
    self.data=data

def path(node, arr,c) :
  if node==None:
    return
  arr.append(node.data)
  path(node.left,arr,c)
  path(node.right,arr,c)
  if node.left==None and node.right==None:
    print(arr)
    if arr not in c:
      c.append(arr)
  arr.pop()
  
root = node(1)
root.left        = node(2);
root.right       = node(3);
root.left.left  = node(4);
root.left.right = node(5); 
s=[]
c1=[]
path(root,s,c1) 

