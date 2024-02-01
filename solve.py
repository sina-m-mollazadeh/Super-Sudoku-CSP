M=9
def solve(grid, row, col, num,constraints):
    for x in range(9):
        if grid[row][x] == num:
            return False
            
    for x in range(9):
        if grid[x][col] == num:
            return False


    for constraint in constraints:
        total = sum(grid[i][j] for i, j in (constraint)[0])
        if total==(constraint)[1][0]:
            return False
        
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    

    return True

def Suduko(grid, row, col,constraint):

    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1,constraint)
    for num in range(1, 10, 1): 
    
        if solve(grid, row, col, num,constraint):
        
            grid[row][col] = num
            if Suduko(grid, row, col + 1,constraint):
                return True
        grid[row][col] = 0
    return False