# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ListNode import ListNode


class Solution:

    #迭代 
    def reverseN(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


    def printList(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next
    

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # Solution().printList(head)
    print("-----------------")
    Solution().printList(Solution().reverseN(head, head.next.next))
    