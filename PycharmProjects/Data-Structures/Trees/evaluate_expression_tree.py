class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def evaluateExpressionTree(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.data)

    left_sum = evaluateExpressionTree(root.left)
    right_sum = evaluateExpressionTree(root.right)

    if root.data == '+':
        return left_sum + right_sum

    elif root.data == '-':
        return left_sum - right_sum

    elif root.data == '*':
        return left_sum * right_sum

    else:
        return left_sum / right_sum


root = node('+')
root.left = node('*')
root.left.left = node('5')
root.left.right = node('4')
root.right = node('-')
root.right.left = node('100')
root.right.right = node('20')
print(evaluateExpressionTree(root))
