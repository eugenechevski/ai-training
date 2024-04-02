import pandas as pd

# Load the Excel file
excel_file_path = './Hospital_Survey_Data_Alcohol_Drug_Abuse.xlsx'
df_excel = pd.read_excel(excel_file_path)

# Load the CSV file
csv_file_path = './Hospital_Survey_Data_Speticemia.csv'
df_csv = pd.read_csv(csv_file_path)

# Correcting the approach to ensure 'Average Covered Charges' is converted to numeric properly
# We need to ensure we handle cases where the conversion has already been applied or is not needed.

# Reattempt the conversion, ensuring we handle non-string types gracefully
def convert_to_numeric(column):
    try:
        return pd.to_numeric(column.str.replace('[\$,]', '', regex=True), errors='coerce')
    except AttributeError:
        # If the column is already numeric or doesn't support str operations, return as is
        return pd.to_numeric(column, errors='coerce')

for df in [df_excel_clean, df_csv_clean]:
    df['Total Discharges'] = convert_to_numeric(df['Total Discharges'])
    df['Average Covered Charges'] = convert_to_numeric(df['Average Covered Charges'])

# Combine the cleaned dataframes
combined_clean_df = pd.concat([df_excel_clean, df_csv_clean])

# Group by state and calculate the sum of discharges and average of medical payments
grouped_clean = combined_clean_df.groupby('State').agg(
    Total_Discharges=('Total Discharges', 'sum'),
    Average_Medical_Payments=('Average Covered Charges', 'mean')
).reset_index()

grouped_clean