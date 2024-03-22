"""
Prompt: How does air quality affect mental health and wellness?
"""

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("./Cities with the Best Work-Life Balance 2022.csv")

# Display descriptive statistics for the specified columns
print(df[['Happiness, Culture & Leisure', 'Air Quality', 'Access to Mental Healthcare']].describe())