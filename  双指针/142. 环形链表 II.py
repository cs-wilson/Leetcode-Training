# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from typing import Optional

from ListNode import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 

        while fast and fast.next: # 快慢指针
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # 相遇
                break
        if not fast or not fast.next:   
            return None
        slow = head  # slow回到起点
        while slow != fast: # slow和fast同时走，相遇的地方就是环的入口
            fast = fast.next 
            slow = slow.next
        return slow     


# @lc code=end
solu = Solution()
print(solu.detectCycle(ListNode([3, 2, 0, -4])))