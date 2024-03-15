df['approximately amount spent per night'] = pd.to_numeric(df['approximately amount spent per night'].str.replace("[^\d\-+\.]", "", regex=True), errors='coerce')
