# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        dummy.next = head

        x = self.findNthNode(dummy, n+1)   
        x.next = x.next.next
        return dummy.next

    def findNthNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head

        index = 0
        while index < n:
            p1 = p1.next
            index += 1

        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2

        

