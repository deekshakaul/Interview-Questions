#Program to print the top view of binary tree
# Use level order traversal and vertical order traversal.

horizontal_distance=[]

class node:
  def __init__(self,data=0):
    self.data=data
    self.left=None
    self.right=None
    self.horizontal_distance=0
    
def Level_order_traversal(root):
    if root is None:
        return
    queue = []
    res=[]
    queue.append(root)
    while(len(queue) > 0):
        res.append(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

#find_horizontal_distance and traverse together calculate and store the horizontal distance of each node
def find_horizontal_distance(root,horizontal_distance):
    if root==None:
      return
    else:
        root.horizontal_distance=horizontal_distance
        if root.left!=None:
            find_horizontal_distance(root.left,horizontal_distance-1)
        if root.right!=None:
            find_horizontal_distance(root.right,horizontal_distance+1)
    
def traverse(root):
  if root==None:
    return 
  traverse(root.left)
  horizontal_distance.append((root.horizontal_distance,root.data))
  traverse(root.right)

#driver code 
bucket=[]
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.right=node(4)
root.right.left=node(7)
root.left.right.left=node(5)
root.left.right.left.left=node(6)
root.right.right=node(8)
root.right.right.right=node(9)

#find level order traversal of the tree
res=Level_order_traversal(root)

#find horizontal distances of the nodes and store tham in buckets according to 
#their horizontal distance

find_horizontal_distance(root,0)
traverse(root)
horizontal_distance.sort(key=lambda x: x[0])
pair1=horizontal_distance[0]
pair2=horizontal_distance[-1]
bucketmin=pair1[0]
bucketmax=pair2[0]

#create bucket
for i in range(bucketmin,bucketmax+1):
  bucket.append([])
for i in horizontal_distance:
  bucket[i[0]-bucketmin].append(i[1])
  
#sort elements in each bucket element such that the node appearing first in level 
#order traversal is at the top
for i in bucket:
  i.sort(key=lambda x: res.index(x))
#print top view  
for i in bucket:
  print(i[0],end=' ')
