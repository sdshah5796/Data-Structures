class getNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorderTraversal(root):
    if root:
        print(root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)



def inordertraversal(root, arr):
    if not root:
        return

    inordertraversal(root.left,arr)
    arr.append(root.data)
    inordertraversal(root.right,arr)


def replaceNodeWithSum(root,arr,i):
    if not root:
        return
    replaceNodeWithSum(root.left, arr, i)
    root.data = arr[i[0]-1] + arr[i[0]+1]
    i[0] +=1
    replaceNodeWithSum(root.right,arr,i)

def replaceNodeWithSumUtil(root):
    if not root:
        return

    arr = []
    arr.append(0)

    inordertraversal(root, arr)
    arr.append(0)
    i = [1]
    replaceNodeWithSum(root,arr,i)


if __name__ == '__main__':
    # binary tree formation
    root = getNode(1)  # 1
    root.left = getNode(2)  # / \
    root.right = getNode(3)  # 2     3
    root.left.left = getNode(4)  # / \ / \
    root.left.right = getNode(5)  # 4 5 6 7
    root.right.left = getNode(6)
    root.right.right = getNode(7)

    print("Preorder Traversal before",
          "tree modification:")
    preorderTraversal(root)

    replaceNodeWithSumUtil(root)
    print()
    print("Preorder Traversal after",
          "tree modification:")
    preorderTraversal(root)
