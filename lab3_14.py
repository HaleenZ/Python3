def combine_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            min_lines = min(len(lines1), len(lines2))
            for i in range(min_lines):
                combined_line = lines1[i].strip() + " " + lines2[i].strip() + "\n"
                output.write(combined_line)
            
            print("Files combined successfully.")
    except FileNotFoundError:
        print("One or more files not found.")
    except IOError:
        print("An error occurred while combining files.")

# Example usage
file1 = input("Enter the path of the first file: ")
file2 = input("Enter the path of the second file: ")
output_file = input("Enter the path of the output file: ")

combine_files(file1, file2, output_file)
