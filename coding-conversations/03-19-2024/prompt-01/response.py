import pandas as pd

# Read the CSV files
df_top_level_bdc = pd.read_excel("./6X6W_Orange Mototrs.xlsx", sheet_name="Orange Motors - Top Level BDC R")

# Compute the correlation
correlation = df_top_level_bdc['Customer Satisfaction Score'].corr(df_top_level_bdc['Sales Volume (USD)'])

# Print the correlation
print("Correlation between Customer Satisfaction Score and Sales Volume:", correlation)