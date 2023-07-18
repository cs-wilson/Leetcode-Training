# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        a, b = head, head
        for i in range(k):
            if not b:
                return head # 不足k个，不反转, base case
            b = b.next
        
        new_head = self.reverseBetween(a, b)

        a.next = self.reverseKGroup(b, k)

        return new_head


    
    def reverseBetween(self, a: Optional[ListNode], b:Optional[ListNode]) -> Optional[ListNode]:
        pre, cur, nxt = None, a, a

        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre

        




