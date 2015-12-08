'''
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.
'''

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None

def is_subtree(t1, t2):
    if t2 is None:
        return True

    return subtree_checker(t1, t2)


def subtree_checker(r1, r2):
    if r1 is None:
        return False
    elif (r1.data == r2.data) and match_tree(r1, r2):
        return True

    return subtree_checker(r1.left, r2) or subtree_checker(r1.right, r2)

def match_tree(r1, r2):

    if (r1 is None) and (r2 is None):
        return True
    elif (r1 is None) or (r2 is None):
        return False
    elif (r1.data != r2.data):
        return False
    else:
        return (match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right))


#Test
t1 = Node(20)
t1.left = Node(10)
t1.right = Node(30)
t1.left.right = Node(15)
t1.left.right.right = Node(17)

t2 = Node(10)
t2.right = Node(15)
t2.right.right = Node(17)

print is_subtree(t1, t2)
