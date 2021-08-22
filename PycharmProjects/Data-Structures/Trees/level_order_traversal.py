class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def height(root):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


def level_order_traversal(root):
    h = height(root)
    for i in range(1, h + 1):
        printcurrentlevel(root, i)


def printcurrentlevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printcurrentlevel(root.left, level - 1)
        printcurrentlevel(root.right, level - 1)


def level_order_traversal_using_queue(root):
    if root is None:
        return
    q = []
    q.append(root)
    while (len(q) > 0):
        temp = q.pop(0)
        print(temp.data)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
level_order_traversal(root)
level_order_traversal_using_queue(root)
