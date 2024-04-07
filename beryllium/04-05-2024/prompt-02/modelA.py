import csv
import datetime

def generate_daily_report(csv_file):
    # Initialize variables
    total_transactions = 0
    total_amount = 0
    highest_transaction = 0
    day = None

    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            # Extract the transaction date and amount
            transaction_date = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
            amount = float(row[1])

            # Update totals
            total_transactions += 1
            total_amount += amount

            # Check for the highest transaction
            if highest_transaction < amount or day is None or transaction_date != day:
                highest_transaction = amount
                day = transaction_date

    # Generate and print the report
    print(f"Daily Report for {day}")
    print(f"Total transactions: {total_transactions}")
    print(f"Total amount: ${total_amount:.2f}")
    print(f"Highest transaction: ${highest_transaction:.2f}")

# Replace 'transactions.csv' with the actual path to your CSV file
generate_daily_report('transactions.csv')