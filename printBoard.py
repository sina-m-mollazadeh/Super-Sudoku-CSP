import os
import numpy as np

def print_grid(array):
    array=np.array(array)
    array=array.reshape(1,81)[0]

    # Set ANSI escape code for red text
    red_text = "\033[1;31m"
    # Set ANSI escape code to reset text color
    reset_color = "\033[0m"

    # Calculate the width of the console

    # Calculate the padding to center the grid

    for i in range(9):
        if i % 3 == 0:
            # Print the red top border
            print(f"{red_text}+{'---+' * 8}---+{reset_color}")
        else:
            # Print the red middle border
            print(f"{red_text}+{'   +' * 8}   +{reset_color}")

        
        # Print the red vertical separator
        print(f"{red_text}{reset_color}", end="")
        for j in range(9):
            index = i * 9 + j
            # Print the centered grid element
            print(f" {array[index]:^2} ", end="")
            if j % 3 == 2 and j != 8:
                # Print the red vertical separator
                print(f"{red_text}|{reset_color}", end="")
        # Print the red vertical separator and move to the next line
        print(f"{red_text}{reset_color}")

    # Print the red bottom border
    print(f"{red_text}+{'---+' * 8}---+{reset_color}")