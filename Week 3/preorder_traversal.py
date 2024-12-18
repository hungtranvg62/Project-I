class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # If the tree is empty, set the root as the new key
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):
        # If key already exists, do not insert it
        if key == node.key:
            return
        elif key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive(node.left, key)
        else:  # key > node.key
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive(node.right, key)

    def preorder_traversal(self):
        result = []
        self.preorder_recursive(self.root, result)
        return result

    def preorder_recursive(self, node, result):
        if node:
            result.append(node.key)  # Visit the node
            self.preorder_recursive(node.left, result)  # Traverse the left subtree
            self.preorder_recursive(node.right, result)  # Traverse the right subtree

# Input and processing
bst = BST()
while True:
    command = input().strip()
    if command == "#":
        break
    if command.startswith("insert"):
        _, key = command.split()
        bst.insert(int(key))

# Output the pre-order traversal
preorder_result = bst.preorder_traversal()
print(" ".join(map(str, preorder_result)))
