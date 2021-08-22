class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder_traversal_recurrsion(root):
    if root:
        inorder_traversal_recurrsion(root.left)
        print(root.data, end = " ")
        inorder_traversal_recurrsion(root.right)

def inorder_traversal_without_recurrsion(root):
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    inorder_traversal_recurrsion(root)
    print()
    inorder_traversal_without_recurrsion(root)