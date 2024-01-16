import numpy as np
from math import floor
from solve import isValid
import os

from printBoard import print_grid

console_width = os.get_terminal_size().columns
os.system('cls' if os.name == 'nt' else 'clear')
pad1=floor((console_width-7)/2)
pad2=floor((console_width-23)/2)
print("*"*pad1,"Welcome","*" *pad1)
print("+"*pad2,"Please Enter the Sudoku","+" *pad2)
print("")

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

array1D=array.reshape(1,81)
left_conditions=[]
right_conditions=[]


for i in range(len(left_numbers)):
    if(len(left_numbers[i])==1):
        array[0][(left_numbers[i])[0]]=(right_numbers[i])[0]
    else:
        left_conditions.append(left_numbers[i])
        right_conditions.append(right_numbers[i])
#now we have a fixed Sudoku table and we are ready to do pruning and .....
def generate_solutions(n, k, current_solution=[]):
    if k == 0:
        # Check if the current solution satisfies the equation sum
        if sum(current_solution) == n:
            yield tuple(current_solution)
        return

    for i in range(11):  # Values from 0 to 10 (inclusive)
        # Try the current value
        current_solution.append(i)

        # Recursively generate solutions for the remaining variables
        yield from generate_solutions(n, k - 1, current_solution)

        # Backtrack: remove the last value to try the next one
        current_solution.pop()

array2D=[]
#Do what is neccesary
for i in range(len(right_conditions)):
    sumInside=0
    count=0
    index=[]
    for j in left_conditions[i]:
        if(array1D[0][j]!=0):
            sumInside+=array1D[0][j]
        else:
            count+=1
            index.append(j)
        
    listS=list(generate_solutions((right_conditions[i])[0]-sumInside,count))
    if(len(listS)==1) and (listS[0])[0]<10:
        array1D[0][index[0]]=(listS[0])[0]


        
    array2D=array1D.reshape(9,9)

#rest
isValidTemp=True
for i in range(9):
    if(isValid(array2D,i)==False):
        print("No")
        exit()
print_grid(array1D[0])