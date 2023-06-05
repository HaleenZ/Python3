import random

def read_random_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
            return random_line.strip()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")

random_line = read_random_line(file_path)
if random_line is not None:
    print("Random line from the file:", random_line)
