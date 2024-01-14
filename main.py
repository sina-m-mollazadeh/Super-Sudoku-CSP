import numpy as np
from math import floor
import os

from printBoard import print_grid

console_width = os.get_terminal_size().columns
os.system('cls' if os.name == 'nt' else 'clear')
pad1=floor((console_width-8)/2)
pad2=floor((console_width-24)/2)
print("*"*pad1,"Welcome","*" *pad1,end="")
print("+"*pad2,"Please Enter the Sudoku","+" *pad2,end="")


#all the inputs
array = []
for _ in range(9):
    row_input = input().split()
    row = [int(num) for num in row_input]
    array.append(row)
formatted_input = []
num_cases = int(input())


left_numbers=[]
right_numbers=[]
for _ in range(num_cases):
    case_input = input().split()
    split_index = case_input.index('>')
    left_numbers.append([int(num) for num in case_input[:split_index]])
    right_numbers.append([int (num) for num in case_input[split_index + 1:]])


array=np.array(array)
array=array.reshape(1,81)
left_conditions=[]
right_conditions=[]


for i in range(len(left_numbers)):
    if(len(left_numbers[i])==1):
        array[0][(left_numbers[i])[0]]=(right_numbers[i])[0]
    else:
        left_conditions.append(left_numbers[i])
        right_conditions.append(right_numbers[i])
#now we have a fixed Sudoku table and we are ready to do pruning and .....
        

print_grid(array[0])