import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("./ttc-bus-delay-data-2022.csv")

# Plot histogram of `Min Delay`
df['Min Delay'].hist()

# Display plot
plt.show()

# Display boxplot of `Min Delay`
df.boxplot(column = ['Min Delay'])

# Display plot
plt.show()

# Sort by `Date`
df_sorted = df.sort_values(by='Date')

# Plot line plot of `Min Delay` by `Date`
plt.plot(df_sorted['Date'], df_sorted['Min Delay'])

# Set title and axis labels
plt.title('Min Delay Over Time')
plt.xlabel('Date')
plt.ylabel('Min Delay')

# Display plot
plt.show()

# Filter the data to only include dates in January 2022
df_jan = df_sorted[(df_sorted['Date'].dt.month == 1)]

# Sort by `Date`
df_jan_sorted = df_jan.sort_values(at='Date')

# Plot line plot of `Min Delay` by `Date`
plt.plot(df_jan_sorted['Date'], df_jan_sorted['Min Delay'])

# Set title and axis labels
plt.title('Min Delay in January 2022')
plt.xlabel('Date')
plt.ylabel('Min Delay')

# Display plot
plt.show()

# Group by `Day` and calculate the mean of `Min Delay`
df_grouped = df.groupby('Day')['Min Delay'].mean()

# Sort by `Day`
df_grouped = df_grouped.sort_values()

# Display a bar chart of the mean `Min Delay` by `Day`
plt.bar(df_grouped.index, df_grouped.values)

# Set the title and axis labels
plt.title('Average Min Delay by Day of Week')
plt.xlabel('Day')
plt.ylabel('Average Min Delay')

# Display plot
plt.show()
