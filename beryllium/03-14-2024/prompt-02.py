"""
    Prompt: Write a Python function that reads a CSV file containing a list of names and email addresses, 
    filters out any rows where the email address is missing, and then writes the filtered data to a new CSV file. 
    Please include error handling for cases where the file might not exist, and use the csv module.
"""

import csv

def modelA():
    def clean_csv_data(input_filename, output_filename):
        # Try to open the input file, handle FileNotFoundError
        try:
            with open(input_filename, 'r') as input_file:
                reader = csv.DictReader(input_file)
        except FileNotFoundError as e:
            print(f"Error: Input file '{input_filename}' not found. Aborting.")
            exit(1)

        # List to hold the filtered data
        filtered_data = []

        # Read each row from the CSV file and append to filtered_data if email is present
        for row in reader:
            if 'email' in row and row['email'] != '':
                filtered_data.append(row)

        # Try to open the output file, handle FileNotFoundError
        try:
            with open(output_filename, 'w', newline='') as output_file:
                writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
                writer.writeheader()  # Write the header to the output file
                writer.writerows(filtered_data)  # Write the filtered rows to the output file
        except FileNotFoundError as e:
            print(f"Error: Output file '{output_filename}' not found. Aborting.")
            exit(1)

        print(f"Successfully filtered and wrote data to '{output_filename}'.")
        
    return clean_csv_data('./contacts.csv', './filtered-contacts-A.csv')

def modelB():
    def filter_csv_file(input_file_name, output_file_name):
        try:
            # Open the input CSV file in read mode
            with open(input_file_name, 'r') as input_file:
                # Read the CSV file using the csv module
                reader = csv.reader(input_file)

                # Create a new empty list to store the filtered data
                filtered_data = []

                # Iterate through each row in the CSV file
                for row in reader:
                    # Check if the email address is present in the current row
                    if len(row) > 1 and row[1]:
                        # Add the row to the filtered data list if the email address is not empty
                        filtered_data.append(row)

            # Open the output CSV file in write mode
            with open(output_file_name, 'w') as output_file:
                # Write the filtered data to the new CSV file using the csv module
                writer = csv.writer(output_file)
                writer.writerows(filtered_data)

            print(f"Successfully filtered and wrote data to {output_file_name}")
        except FileNotFoundError as e:
            print(f"Error: File {input_file_name} not found.")
        except Exception as e:
            print(f"Error: Unknown error occurred while processing the file.")

    return filter_csv_file('./contacts.csv', './filtered-contacts-B.csv')

modelB()

