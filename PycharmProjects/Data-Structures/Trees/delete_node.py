class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key, end=" ")
    inorder(temp.right)

def delete_node(root, key):
    if not root:
        return
    if root.left is None or root.right is None:
        if root.key == key:
            return None
        else:
            return root

    q = []
    q.append(root)
    key_node = None
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if temp.key == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.key
        key_node.key = x
        deletedeepest(root, temp)
    return root


def deletedeepest(root, d_node):
    q= []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
if __name__=='__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 11
    root = delete_node(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)