#https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    node = ListNode(0)
    result = node
    carry = 0
    while l1!=None or l2!=None:
        if l1!=None:
            node.val += l1.val
            l1 = l1.next
        if l2!=None:
            node.val += l2.val
            l2 = l2.next
        if node.val > 9:
            node.val -= 10
            carry = 1
        else:
            carry = 0
        if l1 == None and l2 == None:
            if carry == 0:
                return result
            else:
                node.next = ListNode(carry)
                node = node.next
                return result
        else:
            node.next = ListNode(carry)
            node = node.next

root1 = ListNode(2)
root1.next = ListNode(4)
root1.next.next = ListNode(3)

root2 = ListNode(5)
root2.next = ListNode(6)
root2.next.next = ListNode(4)

result = addTwoNumbers(root1, root2)

while result!=None:
  if result.next != None:
      print(result.val , end = " -> ")
  else:
      print(result.val)
  result = result.next
