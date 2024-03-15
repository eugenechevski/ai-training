import pandas as pd


# Read the CSV file into a DataFrame
df = pd.read_csv("./Airbnb host customer review.xlsx - Sheet1.csv")

# Remove all characters except numbers, ".", "+" or "-".
df['approximately amount spent per night'] = pd.to_numeric(df['approximately amount spent per night'].astype(str).str.replace("[^\d\-+\.]", "", regex=True), errors='coerce')

# Calculate the Pearson correlation coefficient
correlation = df['What is your age'].corr(df['approximately amount spent per night'])

# Print the correlation coefficient and interpretation
print("Pearson Correlation Coefficient:", correlation)

if correlation > 0.7:
    print("Interpretation: There is a strong positive correlation. Higher age is associated with higher spending.")
elif correlation < -0.7:
    print("Interpretation: There is a strong negative correlation. Higher age is associated with lower spending.")
elif 0.3 < correlation < 0.7 or -0.7 < correlation < -0.3:
    print("Interpretation: There is a moderate positive/negative correlation. Age and spending are somewhat related.")
else:
    print("Interpretation: There is a weak or no linear correlation between age and spending.")