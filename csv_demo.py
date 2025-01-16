import csv
import os

# Get configuration values
file_path = 'utilities/loan_app.csv'
name_to_search = 'Sam'
name_to_add = 'Henry'
amount_to_add = int(2600)
status_to_add = 'Approved'

try:
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, 'r') as read_file:
        file = csv.reader(read_file, delimiter=',')

        n = 0
        names = []
        amounts = []
        status = []

        for row in file:
            try:
                if n > 0:  # Skip the header
                    if len(row) < 3:
                        raise ValueError(
                            f"Row {n} has insufficient columns: {row}")
                    print(f"Row {n}: {row}")
                    names.append(row[0])
                    amounts.append(row[1])
                    status.append(row[2])
                n += 1
            except ValueError as ve:
                print(f"Error processing row {n}: {ve}")

        if n == 0:
            raise ValueError("The file is empty or contains only headers.")

        print(f"Names array: {names}")
        print(f"Amounts array: {amounts}")
        print(f"Status array: {status}")
        print('\n')

        # Search for a name in the list
        if name_to_search in names:
            index = names.index(name_to_search)
            print(f"{name_to_search}'s info found\n************")
            print(f"Amount: {amounts[index]}")
            print(f"Status: {status[index]}")
        else:
            print(f"'{name_to_search}' not found in the data!")

    print('\n************')
    # Check for the new name and write to file if not found
    if name_to_add not in names:
        with open(file_path, 'a', newline='') as write_file:  # Append mode
            writer = csv.writer(write_file)
            writer.writerow([name_to_add, amount_to_add, status_to_add])
            print(f"Added entry for '{name_to_add}'.")
    else:
        print(f"'{name_to_add}' already exists in the data.")

except FileNotFoundError as fnf:
    print(f"File error: {fnf}")
except ValueError as ve:
    print(f"Value error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
