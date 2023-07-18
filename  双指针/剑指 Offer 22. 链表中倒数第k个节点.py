# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        
        index = 0
        while index < k:
            p1 = p1.next
            index += 1
        
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        return p2
        
