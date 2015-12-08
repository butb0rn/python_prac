'''
Implement a function to check if a binary tree is balanced.
'''
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None

def is_balanced(root):
    if height_checker(root) == -1:
        return False
    else:
        return True

def height_checker(root):
    if root:
        left_height = height_checker(root.left)
        if left_height == -1:
            return -1
        right_height = height_checker(root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
    else:
        return 0

root = TreeNode()
root.left = TreeNode()
root.right = TreeNode()
root.right.right = TreeNode()
root.left.left = TreeNode()
root.left.right = TreeNode()
root.left.left.left = TreeNode()
print is_balanced(root)
