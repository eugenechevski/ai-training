def read_first_line(file_path):
    try:
        with open(file_path, 'r') as file:
            return next(file).strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file '{file_path}'.")
        return None


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file '{file_path}'.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read file '{file_path}'.")
        return None


def write_reverse(src_file_path, dest_file_path):
    try:
        # Check if source file exists and is readable
        with open(src_file_path, 'r') as src_file:
            # Check if destination file is writable
            with open(dest_file_path, 'w') as dest_file:
                for line in src_file:
                    # Reverse the content of each line
                    reversed_line = line.strip()[::-1] + '\n'
                    dest_file.write(reversed_line)
    except FileNotFoundError:
        print(f"Error: Source file '{src_file_path}' not found.")
    except IOError:
        print(f"Error: Unable to read source file '{ \
              src_file_path}' or write to destination file '{dest_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


write_reverse("./test.txt", "./reversed.txt")
