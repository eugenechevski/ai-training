import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("ice_email_replies-ice_email_replies.csv")

# Display unique values in the `classificationResult` column and their count
print(df['classificationResult'].value_counts())                  