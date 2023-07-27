# 广度优先搜索函数

from TreeNode import TreeNode


def bfs(root):
    if root is None:
        return
    
    queue = []  # 使用队列来存储待访问的节点
    queue.append(root)  # 将根节点加入队列
    
    while queue:
        node = queue.pop(0)  # 取出队列头部的节点
        
        # 处理当前节点
        print(node.val)
        
        # 将当前节点的子节点加入队列
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# 创建一个二叉树示例
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 调用广度优先搜索函数进行遍历
bfs(root)