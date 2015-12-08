'''
Given a sorted(increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
and also we created in_order, pre_order, and post_order to check the result.
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_minimal_tree(items):
    return minimal_tree(items, 0, len(items) - 1)

def minimal_tree(items, start, end):
    if end < start: return None
    mid = (start + end) / 2
    n = TreeNode(items[mid])
    n.left = minimal_tree(items, start, mid - 1)
    n.right = minimal_tree(items, mid + 1, end)
    return n

def inOrder_traversal(node):
    if node:
        inOrder_traversal(node.left)
        print node.data
        inOrder_traversal(node.right)

def preOrder_traversal(node):
    if node:
        print node.data
        preOrder_traversal(node.left)
        preOrder_traversal(node.right)

def postOrder_traversal(node):
    if node:
        postOrder_traversal(node.left)
        postOrder_traversal(node.right)
        print node.data

items = [4, 5, 6, 7, 15, 23, 50, 71]
tree = create_minimal_tree(items)
inOrder_traversal(tree)
#4->5->6->7->15->23->50->71
# preOrder_traversal(tree)
#7->5->4->6->23->15->50->71
# postOrder_traversal(tree)
#4->6->5->15->71->50->23->7
