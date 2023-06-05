def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return ''.join(lines[:n])
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")
num_lines = int(input("Enter the number of lines to read: "))

file_contents = read_first_n_lines(file_path, num_lines)
if file_contents:
    print("First", num_lines, "lines:")
    print(file_contents)
