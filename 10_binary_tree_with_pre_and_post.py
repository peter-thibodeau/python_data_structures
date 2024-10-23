class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
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

    def in_order(self):
        return self._in_order_rec(self.root)

    def _in_order_rec(self, node): # in order traversal
        return (self._in_order_rec(node.left) + [node.value] +
                self._in_order_rec(node.right)) if node else []

    def pre_order(self): # pre order traversal
        return self._pre_order_rec(self.root)

    def _pre_order_rec(self, node):
        return ([node.value] + self._pre_order_rec(node.left) +
                self._pre_order_rec(node.right)) if node else []

    def post_order(self):
        return self._post_order_rec(self.root) # post order traversal

    def _post_order_rec(self, node):
        return (self._post_order_rec(node.left) +
                self._post_order_rec(node.right) + [node.value]) if node else []

if __name__ == "__main__":
    tree = BinaryTree() # Create an instance of the binary tree class
    nodes = [15, 10, 20, 8, 12, 17, 25] # insert all the nodes
    for node in nodes:
        tree.insert(node)

    # Test cases
    in_order_result = tree.in_order()
    print("In-order Traversal:", in_order_result)

    pre_order_result = tree.pre_order()
    print("Pre-order Traversal:", pre_order_result)

    post_order_result = tree.post_order()
    print("Post-order Traversal:", post_order_result)
