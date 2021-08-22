class Node:

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key, end=" ")
    inorder(temp.right)

def isOperator(element):
    if element == "+" or element == "-" or element == "*" or element == "/" or element == "%":
        return True
    else:
        return False

def expression_tree(postfix):
    stack = []
    for char in postfix:
        if not isOperator(char):
            node1 = Node(char)
            stack.append(node1)
        else:
            node1 = Node(char)
            op1 = stack.pop()
            op2 = stack.pop()
            node1.right = op1
            node1.left = op2
            stack.append(node1)
    node = stack.pop()
    return node
postfix = "ab+ef*g*-"
r = expression_tree(postfix)
print("Infix expression is")
inorder(r)

