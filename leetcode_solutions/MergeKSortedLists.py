# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for l in lists:
            while l!= None:
                heap.append(l.val)
                l = l.next
        heapq.heapify(heap)
        result = ListNode()
        head = result
        while len(heap) > 0:
            result.next = ListNode(heapq.heappop(heap))
            result = result.next
        return head.next
