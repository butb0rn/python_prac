def zero_matrix(matrix):
    print matrix #given matrix
    i_flag = False
    j_flag = False

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            j_flag = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            i_flag = True
            break

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1,len(matrix)):
        if matrix[i][0] == 0:
            i_zerofy(matrix, i)

    for j in range(1,len(matrix[0])):
        if matrix[0][j] == 0:
            j_zerofy(matrix, j)

    if i_flag:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    if j_flag:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    print matrix #result

def i_zerofy(matrix, i):
    for k in range(1,len(matrix[0])):
        matrix[i][k] = 0


def j_zerofy(matrix, j):
    for k in range(1,len(matrix)):
        matrix[k][j] = 0



matrix = [[None]*3 for i in range(5)]
matrix[4][2] = 0
matrix[1][1] = 0
zero_matrix(matrix)
