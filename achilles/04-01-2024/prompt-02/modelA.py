import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv("./E22_ Combo 2 (FAL Projects NY - West SM.tsv, FAL Projects NY - office NY - FAL Proyectos.xlsx", sep="\t")

print(df.head())

