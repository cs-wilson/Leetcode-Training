# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow ,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        
        left, right = head, self.reverse(slow)

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        pre, cur, nxt = None, head, head 
        while cur:
            nxt = cur.next
            cur.next = pre 
            pre = cur 
            cur = nxt
        return pre 
