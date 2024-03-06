import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('Netflix_TV_Shows_and_Movies.csv')

# Display the first 5 rows
print(df.head())

# Get information about the columns
print(df.info())

# Check for duplicate rows
num_duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")

# Count values in categorical columns (e.g., 'Type', 'Listed_in')
for col in df.select_dtypes(include='object').columns:
  print(f" \
'Value counts for column '{col}':")
  print(df[col].value_counts())

# Describe numerical columns (e.g., 'Duration')
for col in df.select_dtypes(include='number').columns:
  print(f" \
'Descriptive statistics for column '{col}':")
  print(df[col].describe())
                  
# Split into DataFrames for movies and TV shows
movies = df[df['type'] == 'MOVIE'].copy()
tv_shows = df[df['type'] == 'SHOW'].copy()

# Convert 'release_year' to numeric for both DataFrames
for df in [movies, tv_shows]:
  df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

import matplotlib.pyplot as plt

# Function to plot histograms with common formatting
def plot_histogram(df, column, title, bins=10, max_value=None):
  plt.figure(figsize=(8, 6))
  plt.hist(df[column].dropna(), bins=bins, edgecolor='black', alpha=0.8)
  if max_value:
    plt.xlim(0, max_value)
  plt.xlabel(column)
  plt.ylabel('Frequency')
  plt.title(title)
  plt.show()

# Plot release year histograms
for df, title in zip([movies, tv_shows], ['Movie Release Years', 'TV Show Release Years']):
  plot_histogram(df, 'release_year', title, bins=10, max_value=2025)

# Plot runtime histograms (up to 300 minutes)
for df, title in zip([movies, tv_shows], ['Movie Runtimes', 'TV Show Runtimes']):
  plot_histogram(df, 'runtime', title, bins=10, max_value=300)

# Function to get and plot top genres/countries
def plot_top_values(df, column, title, top_n=10):
  top_values = df[column].value_counts().nlargest(top_n)
  plt.figure(figsize=(8, 6))
  plt.bar(top_values.index, top_values.values)
  plt.xlabel(column)
  plt.ylabel('Count')
  plt.title(f"Top {top_n} {title}")
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()

# Plot top genres for movies and TV shows
for df, kind in zip([movies, tv_shows], ['Movies', 'TV Shows']):
  plot_top_values(df, 'genres', f"Top Genres in {kind}")

# Plot top production countries for movies and TV shows
for df, kind in zip([movies, tv_shows], ['Movies', 'TV Shows']):
  plot_top_values(df, 'production_countries', f"Top Production Countries in {kind}")

# Concatenate DataFrames back together
df = pd.concat([movies, tv_shows], ignore_index=True)

                  