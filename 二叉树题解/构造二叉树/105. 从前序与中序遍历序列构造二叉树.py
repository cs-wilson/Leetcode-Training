# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return None

        root_val = preorder[0]
        root_val_index = inorder.index(root_val)
        root = TreeNode(root_val)

        left_inorder_tree = inorder[ : root_val_index]
        right_inorder_tree = inorder[root_val_index + 1 : ]

        left_preorder_tree = preorder[1: root_val_index + 1]
        right_preorder_tree = preorder[root_val_index + 1 : ]

        root.left = self.buildTree(left_preorder_tree, left_inorder_tree)
        root.right = self.buildTree(right_preorder_tree, right_inorder_tree)

        return root
    
    def printTree(self, root: Optional[TreeNode]):
        if root is None:
            return
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)



solution = Solution()
root = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
solution.printTree(root)