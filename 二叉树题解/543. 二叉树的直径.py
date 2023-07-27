# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.ans

    

    def maxDepth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        
        left_len = self.maxDepth(root.left)
        right_len = self.maxDepth(root.right)
        self.ans = max(self.ans, left_len + right_len)  # 维护子树中的最大直径
        return max(left_len, right_len) + 1

