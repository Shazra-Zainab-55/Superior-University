class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent 
        self.position = position  
        self.g = 0 
        self.h = 0 
        self.f = 0  
    def __eq__(self, other):
        return self.position == other.position
def a_star(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = [start_node]  
    closed_list = [] 
    while open_list:
        open_list.sort(key=lambda x: x.f)
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        if current_node == end_node:
            return retrace_path(current_node)
        children = get_children(current_node, maze)
        for child in children:
            if child in closed_list:
                continue
            child.g = current_node.g + 1
            child.h = heuristic(child.position, end_node.position)
            child.f = child.g + child.h
            if add_to_open(open_list, child):
                open_list.append(child)
    return None
def get_children(node, maze):
    children = []
    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  
        pos = (node.position[0] + move[0], node.position[1] + move[1])
        if (0 <= pos[0] < len(maze) and 
                0 <= pos[1] < len(maze[0]) and 
                maze[pos[0]][pos[1]] == 0):
            children.append(Node(node, pos))
    return children

def heuristic(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def add_to_open(open_list, child):
    return all(child != node or child.g < node.g for node in open_list)

def retrace_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0) 
end = (4, 4)    
path = a_star(maze, start, end)
print("Path from start to end:", path)
