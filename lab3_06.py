def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return ''.join(lines)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")

file_contents = read_file_lines(file_path)
if file_contents:
    print("File contents:")
    print(file_contents)
