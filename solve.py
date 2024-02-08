# def constraintCheck(grid,row,col,num,constraints):
#     grid[row][col]=num
#     constraints=list(zip(constraints))
#     for i in range(len(constraints)):
#         print("second",row,col)
#         left=(((constraints[i])[0])[0])
#         right=(((constraints[i])[0])[1])[0]
#         total=0
#         for temp in range(0,len(left)):
#             inp=(left)[temp]
#             if(grid[inp[0]][inp[1]]==0):
#                 total=0
#                 break
#             if(grid[inp[0]][inp[1]]!=0):
#                 total+=grid[inp[0]][inp[1]]
#         if(total!=0 and total!=right):
#             grid[row][col]=0
#             return False
#     grid[row][col]=0
#     return True
def constraintCheck(grid, row, col, num, constraints):
    grid[row][col] = num
    
    # Iterate over each constraint
    for constraint in constraints:

        left = constraint[0][0]
        right = constraint[1][0]
        total = 0
        if grid[left[0]][left[1]] == 0:
                total = 0
                break

        total += grid[left[0]][left[1]]
        
        # Check if the total sum matches the constraint
        if total != 0 and total != right:
            grid[row][col] = 0
            return False
    
    # Reset the grid value
    grid[row][col] = 0
    return True




def solve(grid, row, col, num,constraints):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    if(constraintCheck(grid,row,col,num,constraints=constraints)):
        pass
    else:
        return False


    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                grid[row][col]=0

                return False
    
    return True



def Suduko(grid, row, col,constraints):
    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1,constraints)
    for num in range(1, 10, 1): 
        if solve(grid, row, col, num,constraints):
            grid[row][col] = num
            if Suduko(grid=grid,row=row,col=(col + 1),constraints=constraints):
                return True
        grid[row][col] = 0

    return False






def SudukoWithBacktrack(grid, row, col,constraints,candidates):
    if (row == 8 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return SudukoWithBacktrack(grid, row, col + 1,constraints,candidates)
    for num in range(1, 10, 1): 
        if solve(grid, row, col, num,constraints):
            grid[row][col] = num
            candidates.append([row,col,num])
            if SudukoWithBacktrack(grid, row, col + 1,constraints,candidates):
                return True
        grid[row][col] = 0

    backtrack(grid,candidates,constraints)
    return [False,grid]




def backtrack(grid,candidates,constraints):
    row,col,num=candidates[-1]
    for i in range(num,10):
        if(solve(grid,row,col,num,constraints)):
            grid[row][col] = num
            candidates.append([row,col,num])
            return SudukoWithBacktrack(grid,row,col+1,constraints,candidates)
    return False
