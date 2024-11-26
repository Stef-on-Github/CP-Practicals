class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node in the Binary Search Tree
def insert(root, value):
    # If the tree is empty, create a new node
    if root is None:
        return Node(value)
    
    # Otherwise, recur down the tree
    if value < root.data:
        root.left = insert(root.left, value)  # Insert in the left subtree
    elif value > root.data:
        root.right = insert(root.right, value)  # Insert in the right subtree
    
    return root

# Function to search a value in the Binary Search Tree
def search(root, value):
    # Base Case: root is null or value is present at the root
    if root is None or root.data == value:
        return root
    
    # Value is greater than root's data, search in the right subtree
    if value > root.data:
        return search(root.right, value)
    
    # Value is smaller than root's data, search in the left subtree
    return search(root.left, value)

# Function to build the Binary Search Tree from user input
def build_bst():
    num_nodes = int(input("Enter the number of nodes in the BST: "))
    if num_nodes == 0:
        return None

    # Get the root node
    root_value = int(input("Enter the root node value: "))
    root = Node(root_value)

    # Insert other nodes into the BST
    for _ in range(num_nodes - 1):
        value = int(input("Enter a value to insert in the BST: "))
        root = insert(root, value)

    return root

# Main Driver Code
root = build_bst()

# Asking the user to enter a value to search in the Binary Search Tree
search_value = int(input("Enter a value to search in the BST: "))

# Searching the value in the BST
if search(root, search_value):
    print(f"Value {search_value} is present in the Binary Search Tree.")
else:
    print(f"Value {search_value} is NOT present in the Binary Search Tree.")
