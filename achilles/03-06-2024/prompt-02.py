import pandas as pd

df = pd.read_csv("./BoeingOrdersandDeliveries.csv")

# Address the trailing space in 'Delivery Year '
df.rename(columns={"Delivery Year ": "Delivery Year"}, inplace=True)

# Convert 'Delivery Year', 'Delivery Total', and 'Order Total' to numeric,
# removing commas if present, excluding row 9072
df.iloc[9072, :] = None  # Set row 9072 to NaN
df["Delivery Year"] = pd.to_numeric(
    df["Delivery Year"].str.replace(",", "")
).fillna(0).astype(int)
df["Delivery Total"] = pd.to_numeric(
    df["Delivery Total"].str.replace(",", "")
).fillna(0).astype(int)
df["Order Total"] = pd.to_numeric(
    df["Order Total"].str.replace(",", "")
).fillna(0).astype(int)

# Filter for data from 2000 onwards
df_filtered = df[df["Delivery Year"] >= 2000]

# Group by 'Country' and sum 'Order Total'
df_grouped = (
    df_filtered.groupby("Country")["Order Total"]
    .sum()
    .sort_values(ascending=False)
)

# Get the top 10 rows
top_10_countries = df_grouped.head(10)

# Calculate mean Delivery Total for top 10 countries
mean_delivery = df_filtered[
    df_filtered["Country"].isin(top_10_countries.index)
]["Delivery Total"].sum() / 10

print(mean_delivery)