def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")

lines_array = read_file_lines(file_path)
if lines_array:
    print("Lines in the file:")
    for line in lines_array:
        print(line)
