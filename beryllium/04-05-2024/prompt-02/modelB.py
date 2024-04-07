# Import the necessary libraries
import pandas as pd
import datetime

# Define the function to generate the daily report
def generate_daily_report(filename):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename)

    # Calculate the total number of transactions
    total_transactions = df.shape[0]

    # Calculate the total amount
    total_amount = df['Amount'].sum()

    # Find the highest transaction amount
    highest_transaction = df['Amount'].max()

    # Create a report string
    report = f"**Daily Report - {datetime.date.today()}**\n"
    report += f"Total Transactions: {total_transactions}\n"
    report += f"Total Amount: ${total_amount:.2f}\n"
    report += f"Highest Transaction: ${highest_transaction:.2f}\n"

    # Print the report
    print(report)

# Run the script with the specified CSV file
generate_daily_report('transaction_records.csv')