# https://leetcode.com/problems/symmetric-tree/

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def isMirrorImage(root):
    if root is None:
        return True
    return isMirrorImageUtil(root, root)


def isMirrorImageUtil(root1, root2):
    if root1.left is None and root2.right is None:
        return True

    if root1.left is not None and root2.right is not None:
        if root1.data == root2.data:
            return isMirrorImageUtil(root1.left, root2.right) and isMirrorImageUtil(root1.right, root2.left)
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print("Symmetric" if isMirrorImage(root) == True else "Not symmetric")
