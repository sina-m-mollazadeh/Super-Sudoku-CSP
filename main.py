import numpy as np
from math import floor
from read import read_specific_line
from printBoard import print_grid
import os
from printBoard import print_grid
from solve import solve_sudoku



os.system('cls' if os.name == 'nt' else 'clear')





console_width = os.get_terminal_size().columns
pad1=floor((console_width-7)/2)
pad2=floor((console_width-23)/2)
print("*"*pad1,"Welcome","*" *pad1)
print("")







#all the inputs
array = []
for i in range(1,10):
    row_input = (str(read_specific_line('testCase.txt',i))).split()
    row = [int(num) for num in row_input]
    array.append(row)
formatted_input = []
num_cases=(int(str((read_specific_line('testCase.txt',10)))))






left_numbers=[]
right_conditions=[]
for i in range(1,num_cases+1):
    case_input = (str(read_specific_line('testCase.txt',i+10))).split()
    split_index = case_input.index('>')
    left_numbers.append([int(num) for num in case_input[:split_index]])
    right_conditions.append([int (num) for num in case_input[split_index + 1:]])





array=np.array(array)
left_conditions=[]
left_conditions = [[[int(digit)-1 for digit in str(number)] for number in sublist] for sublist in left_numbers]




solution = solve_sudoku(array, zip(left_conditions, right_conditions))

# Print the solution
print_grid(solution)