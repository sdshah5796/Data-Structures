class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def build_tree(inorder, preorder):
    if not preorder or not inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(inorder[:mid], preorder[1:mid + 1])
    root.right = build_tree(inorder[mid + 1:], preorder[mid + 1:])
    return root


preorder = [1, 2, 4, 5, 3, 6]
inorder = [4, 2, 5, 1, 3, 6]
build_tree(preorder, inorder)
