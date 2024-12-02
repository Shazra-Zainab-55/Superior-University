class TreeNode:
    def __init__(self, value):
        """Create a tree node with the given value and initialize left/right children as None."""
        self.value = value
        self.left = None 
        self.right = None  
def preorder_traversal(node):
    """Visit nodes in preorder (Root -> Left -> Right) and print their values."""
    if node: 
        print(node.value, end=' ') 
        preorder_traversal(node.left)  
        preorder_traversal(node.right)  
def inorder_traversal(node):
    """Visit nodes in inorder (Left -> Root -> Right) and print their values."""
    if node: 
        inorder_traversal(node.left) 
        print(node.value, end=' ') 
        inorder_traversal(node.right) 
def postorder_traversal(node):
    """Visit nodes in postorder (Left -> Right -> Root) and print their values."""
    if node: 
        postorder_traversal(node.left)  
        postorder_traversal(node.right)  
        print(node.value, end=' ')  
if __name__ == "__main__":
    root = TreeNode(1) 
    root.left = TreeNode(2)  
    root.right = TreeNode(3)  
    root.left.left = TreeNode(4)  
    root.left.right = TreeNode(5) 
    print("Preorder Traversal (Root -> Left -> Right):")
    preorder_traversal(root) 
    print("\n") 
    print("Inorder Traversal (Left -> Root -> Right):")
    inorder_traversal(root) 
    print("\n")  
    print("Postorder Traversal (Left -> Right -> Root):")
    postorder_traversal(root)  
    print("\n")  
