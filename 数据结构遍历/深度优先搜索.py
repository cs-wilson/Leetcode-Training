# 深度优先搜索函数
# 1. 递归终止条件
# 2. 处理当前层逻辑
# 3. 下探到下一层
# 4. 清理当前层
from TreeNode import TreeNode

def dfs(root):
    if root is None:
        return
    
    # 先处理当前节点
    print(root.val)
    
    # 递归遍历左子树
    dfs(root.left)
    
    # 递归遍历右子树
    dfs(root.right)

# 创建一个二叉树示例
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 调用深度优先搜索函数进行遍历
dfs(root)

    