class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to build a binary tree from user input
def build_tree():
    num_nodes = int(input("Enter the number of nodes: "))
    if num_nodes == 0:
        return None
    root_data = input("Enter the root node value: ")
    if root_data.lower() == 'none':
        return None
    root = Node(int(root_data))
    queue = [root]
    count = 1

    while queue and count < num_nodes:
        current = queue.pop(0)
        left_data = input(f"Enter left child of {current.data} (or 'None'): ")
        if left_data.lower() != 'none':
            current.left = Node(int(left_data))
            queue.append(current.left)
            count += 1
        if count >= num_nodes:
            break
        right_data = input(f"Enter right child of {current.data} (or 'None'): ")
        if right_data.lower() != 'none':
            current.right = Node(int(right_data))
            queue.append(current.right)
            count += 1
    return root

# Function to check if the tree is a valid binary tree
def is_binary_tree(root):
    if not root:
        return True  # An empty tree is considered a valid binary tree
    
    # Helper function to check if each node has at most two children
    def check_children(node):
        if not node:
            return True
        # A node should not have more than two children (left and right)
        # Just ensuring that each node has at most one left and one right child
        return (check_children(node.left) and check_children(node.right))

    # Call the helper function on the root node
    return check_children(root)

# Driver Code
root = build_tree()

# Check if the tree is a valid binary tree
if is_binary_tree(root):
    print("The tree is a valid Binary Tree.")
else:
    print("The tree is NOT a valid Binary Tree.")
