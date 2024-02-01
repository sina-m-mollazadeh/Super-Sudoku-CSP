def read_specific_line(file_path, line_number):
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()

        # Check if the line number is within the valid range
        if 1 <= line_number <= len(lines):
            # Return the desired line (subtract 1 because list indices start from 0)
            return lines[line_number - 1]
        else:
            return None