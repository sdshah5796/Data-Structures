class newNode:
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


def spiral(root):
    flag = True
    h = height(root)
    for i in range(1, h + 1):
        printcurrentlevel(root, i, flag)
        flag = not flag


def printcurrentlevel(root, level, flag):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        if flag == False:
            printcurrentlevel(root.left, level - 1, flag)
            printcurrentlevel(root.right, level - 1, flag)
        else:
            printcurrentlevel(root.right, level - 1, flag)
            printcurrentlevel(root.left, level - 1, flag)


def spiral_using_queue(root):
    if root is None:
        return

    s1 = []
    s2 = []
    s1.append(root)
    while (len(s1) != 0 or len(s2) != 0):
        while (len(s1) != 0):
            temp = s1[-1]
            s1.pop()
            print(temp.data, end=" ")
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while (len(s2) != 0):
            temp = s2[-1]
            s2.pop()
            print(temp.data, end=" ")
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print("Spiral Order traversal of binary tree is")
    spiral(root)
    spiral_using_queue(root)
