class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert nodes level-wise to maintain a complete binary tree
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    # Count the total number of nodes in the tree
    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # Check if the tree is complete
    def is_complete(self, node, index, node_count):
        if node is None:
            return True
        if index >= node_count:
            return False
        return (self.is_complete(node.left, 2 * index + 1, node_count) and
                self.is_complete(node.right, 2 * index + 2, node_count))

    # Check if the tree follows the max-heap property
    def is_max_heap_property(self, node):
        if node is None:
            return True

        # If node has no children
        if not node.left and not node.right:
            return True

        # If node has only left child
        if node.left and not node.right:
            return node.data >= node.left.data and self.is_max_heap_property(node.left)

        # If node has both children
        if node.left and node.right:
            return (node.data >= node.left.data and
                    node.data >= node.right.data and
                    self.is_max_heap_property(node.left) and
                    self.is_max_heap_property(node.right))

    # Check if the binary tree is a max-heap
    def is_max_heap(self):
        node_count = self.count_nodes(self.root)
        if self.is_complete(self.root, 0, node_count) and self.is_max_heap_property(self.root):
            return True
        return False

# Drive Code
if __name__ == "__main__":
    bt = BinaryTree()
    n = int(input("Enter the number of elements in the binary tree: "))
    print("Enter the elements:")
    for _ in range(n):
        element = int(input())
        bt.insert(element)

    if bt.is_max_heap():
        print("The binary tree is a max-heap.")
    else:
        print("The binary tree is not a max-heap.")
