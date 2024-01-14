import numpy as np

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




print(left_numbers)
print(right_numbers)
array=np.array(array)
array=array.reshape(1,81)
