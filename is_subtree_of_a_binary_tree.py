class node:

    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def isSame(n1,n2):
  if n1==None and n2==None:
    return True
  if n1 == None or n2==None:
    return False
  return isSame(n1.left,n2.left) and isSame(n1.right,n2.right) and n1.data==n2.data
  
def isSub(n1,n2):
  if n1==None and n2==None:
    return True
  if n2==None:
    return True
  if n1==None:
    return False
  return isSame(n1,n2.left) or isSame(n1,n2.right)
 
root = node(10);
root.left = node(-2);
root.right = node(6);
root.left.left = node(8);
root.left.right = node(-4);
root.right.left = node(7);
root.right.right = node(5);

root2 = node(-3);
root2.left = node(8);
root2.right = node(-4);
a=isSub(root2,root)
print(a)
