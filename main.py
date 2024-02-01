import numpy as np
from math import floor
from solve import valid
from solve import solve
from read import read_specific_line
from printBoard import print_grid
import os


from printBoard import print_grid
os.system('cls' if os.name == 'nt' else 'clear')
input=""





console_width = os.get_terminal_size().columns
pad1=floor((console_width-7)/2)
pad2=floor((console_width-23)/2)
print("*"*pad1,"Welcome","*" *pad1)
print("+"*pad2,"Please Enter the Sudoku","+" *pad2)
print("")




#all the inputs
array = []
for i in range(1,10):
    row_input = (str(read_specific_line('testCase.txt',i))).split()
    print(row_input)
    row = [int(num) for num in row_input]
    array.append(row)
formatted_input = []
num_cases=(int(str((read_specific_line('testCase.txt',10)))))
print(num_cases)


left_numbers=[]
right_numbers=[]
for i in range(1,num_cases+1):
    case_input = (str(read_specific_line('testCase.txt',i+10))).split()
    split_index = case_input.index('>')
    left_numbers.append([int(num) for num in case_input[:split_index]])
    right_numbers.append([int (num) for num in case_input[split_index + 1:]])


array=np.array(array)
left_conditions=[]
right_conditions=[]


# array1D=array.reshape(1,81)[0]
# print_grid(array1D)


