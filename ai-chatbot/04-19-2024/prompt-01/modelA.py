def read_first_line(file_path):
    try:
        with open(file_path, 'r') as file:
            return next(file).strip()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file '{file_path}'.")
        return None
    
def write_reverse(source_file_path, destination_file_path):
    try:
        with open(source_file_path, 'r') as source_file:
            with open(destination_file_path, 'w') as destination_file:
                for line in source_file:
                    reversed_line = line.strip()[::-1] + '\n'
                    destination_file.write(reversed_line)
    except FileNotFoundError:
        print(f"Error: Source file '{source_file_path}' not found.")
    except IOError:
        print(f"Error: Unable to read source file '{source_file_path}' or write to destination file '{destination_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
write_reverse("./test.txt", "./reversed.txt")