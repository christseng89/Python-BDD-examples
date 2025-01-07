def read_file(n=None, start=0) -> None:
    """
    Reads the file with the given number of bytes (n) starting from a specified position (start).
    If n is None, reads the entire content from the start position.

    Best practices by using the 'with' statement, no need to add file.close().
    """
    try:
        # Open the file safely using 'with' statement
        with open('test.txt', 'r') as file:  # 'r' ensures file is opened in read mode

            # Move the cursor to the 'start' position
            file.seek(start)

            # Read n bytes or the rest of the file if n is None
            content = file.read(n)

            # Print the content read
            print(f"Read {n} bytes from position {start} in test.txt:\n\n{content}")
        print('\n')

    except FileNotFoundError:
        print("Error: File 'test.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_line(start=1):
    """
    Reads lines starting from the specified line number (default = 1).
    """
    try:
        # Open the file in read mode
        with open('test.txt', 'r') as file:
            # Skip lines before the start position
            for _ in range(start - 1):  # Move to the start line
                file.readline()

            # Read and print the remaining lines
            print(f"Start from line: {start} \n")
            for n, line in enumerate(file, start=start):
                print(f"Line {n}: {line.strip()}")  # Print line with line number

        print('\n')  # Add spacing after output

    except FileNotFoundError:
        print("Error: File 'test.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
read_file()  # Read the entire file
read_file(9)  # Read first 9 characters
read_file(5, start=3)  # Read 5 characters starting from position 3

# print ('\n')
read_line()
read_line(5)