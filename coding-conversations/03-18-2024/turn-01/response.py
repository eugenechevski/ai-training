import matplotlib.pyplot as plt
import pandas as pd


# Read the CSV file into a DataFrame
df = pd.read_excel('2KEK_ConstructionPrices__PublicLighting.xlsx', sheet_name='public_lighting')

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())

# Remove '$' and ',' from `unit_cost` and convert it to float
df['unit_cost'] = df['unit_cost'].replace('[\$,]', '', regex=True).astype(float)

# Calculate average unit cost per type
avg_unit_cost = df.groupby('type')['unit_cost'].mean()

# Create a new DataFrame
result = pd.DataFrame({'type': avg_unit_cost.index, 'avg_unit_cost': avg_unit_cost.values})

# Sort by average unit cost in descending order
result = result.sort_values(by='avg_unit_cost', ascending=False)

# Plot bar chart
plt.bar(result['type'], result['avg_unit_cost'])
plt.xlabel('Type')
plt.ylabel('Average Unit Cost')
plt.title('Average Unit Cost by Type')
plt.show()