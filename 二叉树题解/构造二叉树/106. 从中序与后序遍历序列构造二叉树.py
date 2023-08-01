# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not (inorder and postorder):
            return None
        root_val = postorder[-1]
        root_index = inorder.index(root_val)

        root = TreeNode(root_val)

        left_inorder = inorder[ : root_index]
        right_inorder = inorder[root_index + 1 : ]

        left_postorder = postorder[ : root_index]
        right_postorder = postorder[root_index:  -1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
    


solution = Solution()
root = solution.buildTree([9,3,15,20,7], [9,15,7,20,3])
