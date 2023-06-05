def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print("List successfully written to the file.")
    except IOError:
        print(f"An error occurred while writing to the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")
data_list = input("Enter the list elements (space-separated): ").split()

write_list_to_file(file_path, data_list)
