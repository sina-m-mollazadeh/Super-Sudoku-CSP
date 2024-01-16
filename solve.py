def findEmpty():
    return "s"
def isValid(matrix,num):
    for row in range(9):
        for col in range(9):
            for i in range(9):
                if matrix[row][i] == num or matrix[i][col] == num:
                    return False
    for row in range(9):
        for col in range(9):
    # Check if the number is not in the same 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if matrix[start_row + i][start_col + j] == num:
                        return False
def applyConstraints():
    return "s"

def generate_solutions(n, k, partial_solution=None):
    if partial_solution is None:
        partial_solution = []

    if k == 0:
        if n == 0:
            yield tuple(partial_solution)
        return

    for i in range(n + 1):
        yield from generate_solutions(n - i, k - 1, partial_solution + [i])

