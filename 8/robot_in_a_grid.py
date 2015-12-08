'''
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are 'off limits' such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the
bottom right. 
'''
class Point:
    def __init__(self, r, c):
        self.c = c
        self.r = r

def find_path(maze):
    cell = Point(0,0)
    path = [cell]
    path_explore(maze, 0, 0, path)
    for cell in path:
        print "[%i,%i]" % (cell.r, cell.c)

def path_explore(maze, r, c, path):
    down = 0
    right = 0
    if maze[r][c] == 1:
        return 1
    elif maze[r][c] == -1:
        path.pop()
        return -1
    else:
        if (r < len(maze)) and (c+1 < len(maze[0])):
            cell = Point(r, c+1)
            path.append(cell)
            right = path_explore(maze, r, c+1, path)
            if right == 1:
                return 1
        else:
            right = -1

        if right == -1:
            if r+1 < len(maze) and c < len(maze[0]):
                cell = Point(r+1, c)
                path.append(cell)
                down = path_explore(maze, r+1, c, path)
                if down == 1:
                    return 1
            else:
                down = -1

        if (right == -1) and (down == -1):
            path.pop()
            return -1



#test
maze = [ [0,0,-1,0,0,0],
         [0,-1,0,0,-1,0],
         [0,0,-1,-1,0,0],
         [0,0,0,0,-1,0],
         [-1,-1,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,-1,-1,-1],
         [0,0,0,0,0,1],
       ]

print maze
find_path(maze)
