# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val >= x:
                p2.next = head
                p2 = p2.next
            else:
                p1.next = head
                p1 = p1.next
                
            head = head.next
            # temp = head.next
            # head.next = None
            # head = temp
        
        p2.next = None
        p1.next = dummy2.next
    
        return dummy1.next