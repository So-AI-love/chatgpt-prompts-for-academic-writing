# Function to read the next line from a file
def get_next_line_from_file(file_path, current_line):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if current_line < len(lines):
                return lines[current_line].strip(), current_line + 1
            else:
                return None, current_line
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, current_line
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, current_line
