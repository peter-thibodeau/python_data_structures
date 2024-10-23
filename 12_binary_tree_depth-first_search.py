class Node: # to create instances of the class node
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key): # insert nodes into the tree
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_rec(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_rec(current_node.right, key)

    def in_order_iterative(self): # in order traversal
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def pre_order_iterative(self): # pre order traversal
        result = []
        if self.root is None:
            return result

        stack = [self.root]

        while stack:
            current = stack.pop()
            result.append(current.value)
            # Push right so that left is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    def post_order_iterative(self): # post order traversal
        result = []
        if self.root is None:
            return result

        stack = []
        last_visited_node = None
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            peek_node = stack[-1]
            # If right child exists and traversing node from left child, then move right
            if peek_node.right and last_visited_node != peek_node.right:
                current = peek_node.right
            else:
                # If right child doesn't exist or traversing from right child, visit node
                result.append(peek_node.value)
                last_visited_node = stack.pop()

        return result

if __name__ == "__main__":
    tree = BinaryTree() # Create an instance of the binary tree class
    nodes = [15, 10, 20, 8, 12, 17, 25]
    for node in nodes: # insert all the nodes
        tree.insert(node)

# Test cases
    in_order_result = tree.in_order_iterative()
    print("In-order Traversal:", in_order_result)

    pre_order_result = tree.pre_order_iterative()
    print("Pre-order Traversal:", pre_order_result)

    post_order_result = tree.post_order_iterative()
    print("Post-order Traversal:", post_order_result)
