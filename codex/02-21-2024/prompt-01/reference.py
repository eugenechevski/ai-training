import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Top5000.csv')

# Display the first 5 rows
print(df.head())

# Print the DataFrame's information
print(df.info())

# Print the DataFrame's columns
print(df.columns)
                  
avg_rating_by_genre = df.groupby('gens')['avg_rat'].mean()
avg_rating_by_genre = avg_rating_by_genre.sort_values(ascending=False)

print(avg_rating_by_genre.head(10))

import matplotlib.pyplot as plt

avg_rating_by_genre.head(10).plot.bar()
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.title("Top 10 Genres with Highest Average Ratings")
plt.show()