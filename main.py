import numpy as np
print("Welcome to this sudoku solver")
board=np.array([[6 ,0 ,9 ,0 ,0 ,7 ,0 ,3 ,0],
                [0 ,0 ,0 ,0 ,9 ,0 ,0 ,0 ,6],
                [0 ,2 ,0 ,0 ,0 ,3 ,9 ,4 ,0],
                [0 ,0 ,0 ,0 ,8 ,2 ,7 ,0 ,0],
                [2 ,0 ,8 ,0 ,7 ,0 ,0 ,0 ,3],
                [0 ,0 ,0 ,9 ,1 ,6 ,0 ,8 ,0],
                [0 ,0 ,2 ,0 ,0 ,0 ,0 ,1 ,4],
                [3 ,0 ,4 ,6 ,5 ,0 ,8 ,0 ,0],
                [1 ,0 ,5 ,0 ,0 ,9 ,0 ,0 ,0]])
n=int(input("Please enter the number of cages: "))
listCages=[]
for i in range(n):
    str=input()
    listCages.append(str)
first=listCages[0].split(" ")
print(first)
print(n)
print(board)