import pandas as pd

# Reading the files
sepsis_data = pd.read_csv('./Hospital_Survey_Data_Speticemia.csv') 
alcohol_drug_abuse_data = pd.read_excel('./Hospital_Survey_Data_Alcohol_Drug_Abuse.xlsx')

import re

# Define a function to select columns based on a regex pattern
def select_columns(data, pattern):
    return data.filter(regex=pattern)

# Define the regex pattern for the columns you want to select
pattern = '^(Provider State|Total Discharges|Average Covered Charges \\$|Average Total Payments \\$|Average Medicare Payments \\$|Hospital Rating)$'

# Select the relevant columns from the sepsis data
sepsis_data = select_columns(sepsis_data, pattern)

# Select the relevant columns from the alcohol drug abuse data
alcohol_drug_abuse_data = select_columns(alcohol_drug_abuse_data, pattern)

# Merge the two datasets
merged_data = pd.merge(sepsis_data, alcohol_drug_abuse_data, on='Provider State', suffixes=('_sepsis', '_alcohol_drug_abuse'))

# Display the merged data
print(merged_data.head())