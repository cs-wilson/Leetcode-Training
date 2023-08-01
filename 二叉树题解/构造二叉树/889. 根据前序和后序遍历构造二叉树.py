# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # 找出root节点
        root_val = preorder[0]
        root_index = preorder.index(root_val)
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root
        # 找出左节点
        leftNode_val = preorder[1]
        leftNode_index = postorder.index(leftNode_val)

        #preorder
        left_preorder = preorder[1 : leftNode_index + 2]
        right_preorder = preorder[leftNode_index + 2 : ]

        # 在postorder里找出leftnode之前的序列为左序列
        left_postorder = postorder[ : leftNode_index + 1]
        right_postorder = postorder[leftNode_index + 1 : -1]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)
        return root
        
    
    
