class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None

def list_depths(root):
    table_levels = {}
    current_level = 0
    depths_calculator(root, table_levels, current_level)
    return table_levels


def depths_calculator(root, table_levels, current_level):
    if root is None:
        return

    if table_levels[current_level]:
        list_node = table_levels[current_level]
    else:
        list_node = []
        table_levels[current_level] = list_node

    list_node.append(root)
    depth_calculator(root.left, table_levels, current_level + 1)
    depth_calculator(root.right, table_levels, current_level + 1)

n = Node(10)
list_depths(n)
