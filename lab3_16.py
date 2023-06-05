def remove_newlines(file_path, output_file):
    try:
        with open(file_path, 'r') as file, open(output_file, 'w') as output:
            for line in file:
                line = line.rstrip('\n')
                output.write(line)
        print("Newlines removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while processing the file.")

# Example usage
file_path = input("Enter the path of the input file: ")
output_file = input("Enter the path of the output file: ")

remove_newlines(file_path, output_file)
