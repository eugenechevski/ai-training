import pandas as pd

df = pd.read_csv("./Spotify_2000.csv");

# Recalculate the standard deviation of BPM after cleaning (just in case)
bpm_std = round(df['Beats Per Minute (BPM)'].std(), 2)

# Print the result with an explanation
print(
    "After cleaning and conversion, the standard deviation of Beats Per Minute (BPM) is",
    bpm_std,
    "beats per minute. This indicates how much the BPM values vary from the average tempo.",
)