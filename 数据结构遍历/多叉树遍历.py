# 1.创建一个队列，用于存储要检查的人
# 2.从队列中弹出一个人，检查这个人是否满足条件
# 3.将这个人的朋友加入队列
# 4.重复第2、3步，直到队列为空


def BFS(graph, start, end):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)
    while queue:
        person = queue.pop(0)
        if person == end:
            return True
        for p in graph[person]:
            if p not in visited:
                queue.append(p)
                visited.add(p)
    return False

