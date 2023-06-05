import os

def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while accessing the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")

file_size = get_file_size(file_path)
if file_size is not None:
    print("File size:", file_size, "bytes")
