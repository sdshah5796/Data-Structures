class newNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def IsFoldable(root):
    if root is None:
        return True
    return isFoldableUtil(root.left, root.right)


def isFoldableUtil(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False

    d1 = isFoldableUtil(n1.left, n2.right)
    d2 = isFoldableUtil(n1.right, n2.left)
    return d1 and d2


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.right.left = newNode(5)

if IsFoldable(root):
    print("Tree is foldable")
else:
    print("Tree is not foldable")
