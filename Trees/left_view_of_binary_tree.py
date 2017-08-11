#Program to print the left view of binary tree
# Use level order traversal.

bucket=[]
class node:
  def __init__(self,data=0):
    self.data=data
    self.left=None
    self.right=None
    
def LeftView(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while True:
      length_of_queue=len(queue)
      if length_of_queue==0:
        break
      else:
        bucket.append([])
        while(length_of_queue > 0):
            bucket[-1].append(queue[0].data)
            
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            length_of_queue-=1

#driver code 
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.right=node(4)
root.right.left=node(7)
root.left.right.left=node(5)
root.left.right.left.left=node(6)
root.right.right=node(8)
root.right.right.right=node(9)

LeftView(root)
for i in bucket:
  print(i[0],end=' ')
