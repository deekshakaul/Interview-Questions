# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution(object):
    def swapPairs(self, head):
        newHead = ListNode()
        result = newHead
        while head != None and head.next != None:
            newHead.next = ListNode(head.next.val)
            newHead.next.next = ListNode(head.val)
            head = head.next.next
            newHead = newHead.next.next
        if head != None:
            newHead.next = ListNode(head.val)
        return result.next
            
