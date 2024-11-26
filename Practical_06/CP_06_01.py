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

# Function to check if the binary tree is complete
def is_complete_btree(root):
    if not root:
        return True
    queue = [root]
    found_null = False
    
    while queue:
        current = queue.pop(0)
        if current:
            if found_null:
                return False
            queue.append(current.left)
            queue.append(current.right)
        else:
            found_null = True
    return True

# Function to check if two nodes are cousins
def are_cousins(root, node1, node2):
    def find_parent_and_level(root, node, level=0):
        if not root:
            return None, 0
        if (root.left and root.left.data == node) or (root.right and root.right.data == node):
            return root, level + 1
        left_parent, left_level = find_parent_and_level(root.left, node, level + 1)
        if left_parent:
            return left_parent, left_level
        return find_parent_and_level(root.right, node, level + 1)

    parent1, level1 = find_parent_and_level(root, node1)
    parent2, level2 = find_parent_and_level(root, node2)
    
    return level1 == level2 and parent1 != parent2

# Driver Code
root = build_tree()

# Check if the tree is complete
if is_complete_btree(root):
    print("Complete Binary Tree")
else:
    print("NOT Complete Binary Tree")

# Check if two nodes are cousins
node1 = int(input("Enter the first node to check if it is a cousin: "))
node2 = int(input("Enter the second node to check if it is a cousin: "))
if are_cousins(root, node1, node2):
    print(f"Nodes {node1} and {node2} are cousins.")
else:
    print(f"Nodes {node1} and {node2} are NOT cousins.")
