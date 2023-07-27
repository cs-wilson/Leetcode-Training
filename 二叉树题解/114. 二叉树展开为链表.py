# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = list()
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.traverse(root)
        size = len(self.res)
        for i in range(1, size):
            prev, curr = self.res[i - 1], self.res[i]
            prev.left = None
            prev.right = curr


    
    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.res.append(root)
        self.traverse(root.left)
        self.traverse(root.right)



