class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a new node with the given value into the BST.

        :param value: The value to be inserted into the BST.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        """
        Searches for a node with the given value in the BST.

        :param value: The value to be searched in the BST.
        :return: The node with the given value if found, otherwise None.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def find_min(self):
        """
        Finds the node with the minimum value in the BST.

        :return: The node with the minimum value.
        """
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, current_node):
        if current_node.left is None:
            return current_node
        else:
            return self._find_min_recursive(current_node.left)

    def find_max(self):
        """
        Finds the node with the maximum value in the BST.

        :return: The node with the maximum value.
        """
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, current_node):
        if current_node.right is None:
            return current_node
        else:
            return self._find_max_recursive(current_node.right)

# Example usage:
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.search(4).value)  # Output: 4
print(bst.find_min().value)  # Output: 2
print(bst.find_max().value)  # Output: 8