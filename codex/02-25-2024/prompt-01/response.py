import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("Truck Repairs for 2023 - Sheet1 - Dr. Victoria Gamble.csv")

# Pivot the DataFrame
pivot_table = df.pivot_table(index='Month', columns='Parts', aggfunc='size')

# Create the heatmap
sns.heatmap(pivot_table, annot=True, cmap='coolwarm')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Display the heatmap
plt.savefig('heatmap.png')