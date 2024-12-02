class Network:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self, node_a, node_b):
        if node_a not in self.adj_list:
            self.adj_list[node_a] = []
        if node_b not in self.adj_list:
            self.adj_list[node_b] = []  
        self.adj_list[node_a].append(node_b)  
        self.adj_list[node_b].append(node_a)  
    def bfs(self, starting_node):
        visited = set()  
        traversal_order = [] 
        def bfs_helper(current_level):
            if not current_level:
                return
            next_level = [] 
            for node in current_level:
                if node not in visited:
                    visited.add(node)  
                    traversal_order.append(node)  
                    next_level.extend(self.adj_list.get(node, []))
            bfs_helper(next_level)
        try:
            bfs_helper([starting_node])
        except Exception as e:
            print(f"Oops! An error occurred during BFS: {e}")

        return traversal_order 
if __name__ == "__main__":
    network = Network()
    network.add_edge(1, 2)
    network.add_edge(1, 3)
    network.add_edge(2, 4)
    network.add_edge(3, 5)

    try:
        # Let's see what our BFS traversal looks like starting from node 1
        bfs_result = network.bfs(1)
        print("BFS Traversal Result:", bfs_result)
    except KeyError as e:
        print(f"Uh-oh! KeyError: {e} - Looks like the starting node doesn't exist in the network.")
    except Exception as e:
        print(f"Yikes! An unexpected error occurred: {e}")
