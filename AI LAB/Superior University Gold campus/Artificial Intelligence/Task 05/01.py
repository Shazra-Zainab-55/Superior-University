class Node:
    def __init__(self, value):
        self.value = value
        self.adj_list = []
        self.visited = False
class DFS:
    def __init__(self):
        pass
    def dfs_stack(self, start_node):
        stack = [start_node]
        while stack:
            current_node = stack.pop()
            if not current_node.visited:
                print(f"Visited node: {current_node.value}")
                current_node.visited = True
            for neighbor in current_node.adj_list:
                if not neighbor.visited:
                    stack.append(neighbor)
if __name__ == "__main__":
    node_A = Node('A')
    node_B = Node('B')
    node_C = Node('C')
    node_D = Node('D')
    node_E = Node('E')
    node_A.adj_list = [node_B, node_C]
    node_B.adj_list = [node_D, node_E]
    node_C.adj_list = []
    node_D.adj_list = []
    node_E.adj_list = []
    dfs = DFS()
    dfs.dfs_stack(node_A)
