from main import array
from main import right_conditions
from main import left_conditions

def findEmpty():
    return "s"
def isValid(array):
    return True
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

