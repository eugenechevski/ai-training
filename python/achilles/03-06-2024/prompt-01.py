import pandas as pd

# Read the CSV file into a DataFrame
sales_data = pd.read_csv("sales_memos.csv")



# Function to handle currency conversion, accounting for various formats
def clean_currency_v2(x):
    if isinstance(x, str):
        x = x.replace('Eur', '').replace(
            'u$s', '').replace('USD', '').replace('$', '')
        x = x.replace(',', '').replace('.', '')
        return float(x) / 100  # Assuming the last two digits are cents
    return float(x)


# Apply the function to the 'Commission' column
sales_data['Commission'] = sales_data['Commission'].apply(clean_currency_v2)

# Sum the commissions by date
sales_by_date = sales_data.groupby('Date')['Commission'].sum().reset_index()

# Find the dates with the highest sales
top_sales_dates = sales_by_date.sort_values(
    'Commission', ascending=False).head()

print(top_sales_dates)