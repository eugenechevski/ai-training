import pandas as pd

work_life_balance_data = pd.read_csv("./Cities with the Best Work-Life Balance 2022.csv")

# Select relevant columns for correlation analysis
columns_of_interest = ['Air Quality', 'Access to Mental Healthcare', 'Happiness, Culture & Leisure', 'Wellness and Fitness', 'City Safety']
correlation_data = work_life_balance_data[columns_of_interest]

# Calculate correlation matrix
correlation_matrix = correlation_data.corr()

print(correlation_matrix)
                                    