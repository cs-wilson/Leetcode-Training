# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from 递归反转链表.ListNode import ListNode


class Solution:
    # 递归
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    #迭代 
    def reverseList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur, nxt = None, head, head
        while cur:
            nxt = cur.next # 保存下一个节点
            cur.next = pre  # 反转
            pre = cur # 更新pre
            cur = nxt # 更新cur
        return pre
    
    def printList(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next
    

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().printList(head)
    print("-----------------")
    Solution().printList(Solution().reverseList(head))
    print("-----------------")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().printList(head)
    print("-----------------")
    Solution().printList(Solution().reverseList_2(head))


