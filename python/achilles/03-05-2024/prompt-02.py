# Read data
import pandas as pd

data = pd.read_csv('./mobile-phone-brands-by-country.csv')

# Separate the data into two groups: Asian countries and South American countries
asian_brands = data[data['Region'] == 'Asia']
south_american_brands = data[data['Region'] == 'South America']

# Calculate the median number of brands for each group
median_asian_brands = asian_brands.groupby('Country').size().median()
median_south_american_brands = south_american_brands.groupby('Country').size().median()

print(median_asian_brands, median_south_american_brands)