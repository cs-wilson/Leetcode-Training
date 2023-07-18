# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from  ListNode import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
    
    def reverseN(self, head: Optional[ListNode], n) -> Optional[ListNode]:
        # successor = None
        if n == 1:
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last
    



if __name__ == "__main__":
    print(Solution().reverseN(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))