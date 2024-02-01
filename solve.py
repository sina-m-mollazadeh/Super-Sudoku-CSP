def find_empty(array2D):
    for i in range(len(array2D)):
        for j in range(len(array2D[0])):
            if array2D[i][j] == 0:
                return (i, j)  # row, col
    return None
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def generate_solutions(n, k, partial_solution=None):
    if partial_solution is None:
        partial_solution = []

    if k == 0:
        if n == 0:
            yield tuple(partial_solution)
        return

    for i in range(n + 1):
        yield from generate_solutions(n - i, k - 1, partial_solution + [i])

