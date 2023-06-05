def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found.")
    except IOError:
        print(f"An error occurred while copying the file.")

# Example usage
source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")

copy_file(source_file, destination_file)
