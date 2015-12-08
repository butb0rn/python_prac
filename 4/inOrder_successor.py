'''
Write an algorithm to find the "next" node(in_order successor) of a given node in a binary search tree.
You may assume that each node has a link to its parent.
'''
class TreeNode:
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None
        self.parent = None


def inOrder_succeessor(root):
    if  root is None:
        return None

    if (root.right):
        return left_most_child(root.right)
    else:
        x = root.parent
        q = root
        while x and (x.left is not q):
            q = x
            x = x.parent

        return x

def left_most_child(root):
    if root is None:
        return None

    while root.left:
        root = root.left

    return root


#Test
n = TreeNode(20)
n.parent = None
n.left = TreeNode(10)
n.right = TreeNode(30)
n.left.parent = n
n.right.parent = n
n.left.right = TreeNode(15)
n.left.right.parent = n.left
n.left.right.right = TreeNode(17)
n.left.right.right.parent = n.left.right
n.left.left = TreeNode(5)
n.left.left.parent = n.left
n.left.left.left = TreeNode(3)
n.left.left.right = TreeNode(7)
n.left.left.left.parent = n.left.left
n.left.left.right.parent = n.left.left

result = inOrder_succeessor(n.left.right.right)
print result.data
