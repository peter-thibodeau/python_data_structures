class Node: # to create instances of the class node
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
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

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None:
            return False
        if node.value == key:
            return True
        elif key < node.value:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)


if __name__ == "__main__":
    bst = BinarySearchTree() # create an instance of the BinarySearchTree class
    nodes = [15, 10, 20, 8, 12, 17, 25]
    for node in nodes: # create nodes for the tree
        bst.insert(node)

    # Test cases
    search_values = [10, 17, 30]
    search_results = {value: bst.search(value) for value in search_values}
    print("Search Results:", search_results)