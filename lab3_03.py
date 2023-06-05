def append_text(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text)
        print("Text appended successfully!")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while appending text to the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")
text = input("Enter the text to append: ")

append_text(file_path, text)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Read the updated contents of the file
file_contents = read_file(file_path)
if file_contents:
    print("Updated file contents:")
    print(file_contents)
