def generate_solutions(n, k, partial_solution=None):
    if partial_solution is None:
        partial_solution = []

    if k == 0:
        if n == 0:
            yield tuple(partial_solution)
        return

    for i in range(n + 1):
        yield from generate_solutions(n - i, k - 1, partial_solution + [i])

# Example usage for x1 + x2 + x3 = 10
n = 10
k = 3
solutions = list(generate_solutions(n, k))
print(solutions)
