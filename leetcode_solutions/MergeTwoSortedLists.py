# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        result = ListNode()
        head = result
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
                result = result.next
            else:
                result.next = ListNode(l2.val)
                l2 = l2.next
                result = result.next
        while l1 != None:
            result.next = ListNode(l1.val)
            l1 = l1.next
            result = result.next
        while l2 != None:
            result.next = ListNode(l2.val)
            l2 = l2.next
            result = result.next
        return head.next
                
