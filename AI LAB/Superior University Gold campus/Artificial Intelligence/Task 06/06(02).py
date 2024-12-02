from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
def bfs(start):
    if not start:
        return []
    queue = deque([start])
    visited = []
    while queue:
        current = queue.popleft()
        visited.append(current.value)
        queue.extend(current.children)
    return visited
if __name__ == "__main__":
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children[0].children.extend([Node(4), Node(5)])
    root.children[1].children.append(Node(6))
    print(bfs(root))  
