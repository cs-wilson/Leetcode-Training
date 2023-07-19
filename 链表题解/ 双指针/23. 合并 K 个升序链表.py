# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for listNode in lists:
            while listNode:
                res.append(listNode.val)
                listNode = listNode.next
        
        res.sort(reverse = True)

        dummy = ListNode(None)
        p = dummy
        while res:
            tempNode = ListNode(res.pop())
            p.next = tempNode
            p = p.next
        
        return dummy.next