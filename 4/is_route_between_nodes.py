'''
Given a directed graph, design an algorithm to find out
whether there is a route between two nodes.
'''

def is_route_between_nodes(graph, start, end):
    if start == end: return True
    queue = [start]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
        for node in graph[vertex]:
            if node not in visited:
                if node == end:
                    return True
                else:
                    queue.append(node)
    return False

# create a directed graph
graph = {}
graph[0] = [1]
graph[1] = [2]
graph[2] = [0]
graph[3] = [1, 2]
graph[4] = [1]
print is_route_between_nodes(graph, 0, 3)
