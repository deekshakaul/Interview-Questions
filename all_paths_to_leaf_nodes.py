#To find all paths from root to leaves
class node :
  def __init__(self,data):
    self.left=None
    self.right=None
    self.data=data

#Function to find all relevant paths. arr stores the nodes encountered in a path. p stores the paths
def findPaths(node, arr,p) :
  if node==None:
    return
  arr.append(node.data)
  findPaths(node.left,arr,p)
  findPaths(node.right,arr,p)
  if node.left==None and node.right==None:
    print(arr)
    if arr not in p:
      p.append(arr)
  arr.pop()     

root = node(1)
root.left        = node(2);
root.right       = node(3);
root.left.left  = node(4);
root.left.right = node(5); 
s=[]
paths=[]
# should give output:1,2,4 ; 1,2,5 ; 1,3
findPaths(root,s,paths) 
