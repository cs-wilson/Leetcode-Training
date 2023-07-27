from TreeNode import TreeNode
'''
中序位置主要用在 BST 场景中，你完全可以把 BST 的中序遍历认为是遍历有序数组。
前序位置的代码执行是自顶向下的，而后序位置的代码执行是自底向上的

前序位置是刚刚进入节点的时刻，后序位置是即将离开节点的时刻。

前序位置的代码只能从函数参数中获取父节点传递来的数据，
而后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据。
'''


# 前序遍历
def preorderTraversal(root):
    if root is None:
        return []
    result = []
    result.append(root.val)  # 先访问根节点
    result += preorderTraversal(root.left)  # 递归遍历左子树
    result += preorderTraversal(root.right)  # 递归遍历右子树
    print("preOrderTraversal", result)
    return result

# 中序遍历
def inorderTraversal(root):
    if root is None:
        return []
    result = []
    result += inorderTraversal(root.left)  # 递归遍历左子树
    result.append(root.val)  # 访问根节点
    result += inorderTraversal(root.right)  # 递归遍历右子树
    return result

# 后序遍历
def postorderTraversal(root):
    if root is None:
        return []
    result = []
    result += postorderTraversal(root.left)  # 递归遍历左子树
    result += postorderTraversal(root.right)  # 递归遍历右子树
    result.append(root.val)  # 访问根节点
    return result
'''
使用示例：

假设有如下二叉树：

         1
       / \
      2   3
     / \
    4   5

可以按照以下方式调用上述函数：
'''

# 创建二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 前序遍历
print('前序遍历：', preorderTraversal(root))  # 输出: [1, 2, 4, 5, 3]

# 中序遍历
print('中序遍历：', inorderTraversal(root))  # 输出: [4, 2, 5, 1, 3]

# 后序遍历
print('后序遍历：', postorderTraversal(root))  # 输出: [4, 5, 2, 3, 1]