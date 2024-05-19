class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def find_min(self):
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Min:", bst.find_min())  # Output: Min: 2
print("Max:", bst.find_max())  # Output: Max: 8
print("Search for 4:", bst.search(4).value)  # Output: Search for 4: 4