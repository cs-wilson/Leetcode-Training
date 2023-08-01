
# Definition for a Node.

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None, next: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root, None)
        return root


    
    def traverse(self, cur: Optional[TreeNode], next: Optional[TreeNode]):
        if cur == None:
            return
        cur.next = next
        self.traverse(cur.left, cur.right)
        self.traverse(cur.right, None if cur.next == None else cur.next.left)
        
