class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def continuous_tree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is None:
        return (abs(root.data - root.right.data) == 1) and continuous_tree(root.right)
    if root.right is None:
        return (abs(root.data - root.left.data) == 1) and continuous_tree(root.left)

    return (abs(root.data - root.left.data) and abs(root.data - root.right.data) and continuous_tree(
        root.left) and continuous_tree(root.right))

root = Node(3)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)
print(continuous_tree(root))