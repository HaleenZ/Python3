def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")

num_lines = count_lines(file_path)
if num_lines is not None:
    print("Number of lines in the file:", num_lines)
