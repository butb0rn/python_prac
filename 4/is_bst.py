'''
Implement a function to check if a binary tree is a binary search tree.
'''

class TreeNode():
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None

def is_bst(root):
    return check_bst(root, None, None)

def check_bst(root, mini, maxi):
    if not root:
        return True

    if ((mini is not None) and (root.data <= mini)) or ((maxi is not None) and (root.data > maxi)):
        return False

    if ( not check_bst(root.left, mini, root.data) or not check_bst(root.right, root.data, maxi)):
        return False

    return True


root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.right = TreeNode(15)
root.left.right.right = TreeNode(17)
root.left.left = TreeNode(8)
root.left.left.right = TreeNode(37)
root.left.left.left = TreeNode(3)
print is_bst(root)
