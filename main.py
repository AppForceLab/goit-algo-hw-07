class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Завдання 1: Пошук найбільшого значення
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

    # Завдання 2: Пошук найменшого значення
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.key

    # Завдання 3: Знаходження суми всіх значень у дереві
    def find_sum(self):
        return self._find_sum(self.root)

    def _find_sum(self, node):
        if node is None:
            return 0
        return node.key + self._find_sum(node.left) + self._find_sum(node.right)

# Тестування
bst = BST()
values = [15, 10, 20, 8, 12, 17, 25]
for v in values:
    bst.insert(v)

print("Максимальне значення:", bst.find_max())  # 25
print("Мінімальне значення:", bst.find_min())  # 8
print("Сума всіх значень:", bst.find_sum())  # 107