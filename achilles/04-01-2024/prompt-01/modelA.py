import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv("Hospital_Survey_Data_Alcohol_Drug_Abuse.xlsx - Sheet1.csv")

# Calculate sum of discharges and mean of payments
df_out = df.groupby('Provider State')[['Total Discharges', 'Average Medicare Payments ($)']].agg('sum').reset_index()
df_out = df_out.rename(columns={'Total Discharges':'Discharges', 'Average Medicare Payments ($)':'Avg Medicare Payments'})

# Display the first 5 rows
print(df_out.head(5).to_markdown(index=False))


                  
                  