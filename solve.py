import numpy as np
import itertools

def is_valid(board, constraint):
    total = sum(board[i][j] for i, j in constraint[0])
    # Check if the combination satisfies the constraint
    if total != constraint[1][0]:
        return False

    # Check for no repeated elements in the same row
    for (i, _), num in zip(constraint[0], constraint[1]):
        if np.count_nonzero(board[i][:] == num) > 1:
            return False

    # Check for no repeated elements in the same column
    for (_, j), num in zip(constraint[0], constraint[1]):
        if np.count_nonzero(board[:][j] == num) > 1:
            return False

    # Check for no repeated elements in the same 3x3 block
    block_i, block_j = constraint[0][0][0] // 3, constraint[0][0][1] // 3
    block_values = [board[block_i * 3 + i][block_j * 3 + j] for i in range(3) for j in range(3)]

    for (_, _), num in zip(constraint[0], constraint[1]):
        if block_values.count(num) > 1:
            return False

    return True


def solve_sudoku(board, constraints):
    for constraint in constraints:
        for combination in itertools.product(range(1, 10), repeat=len(constraint[0])):
            temp_board = [row.copy() for row in board]
            for (i, j), num in zip(constraint[0], combination):
                temp_board[i][j] = num

            if is_valid(temp_board, constraint):
                board = temp_board

    return board