import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_prepare_data(file_path):
    """
    Load the air quality data and prepare it for analysis.
    
    Parameters:
    file_path (str): Path to the CSV file containing AQI data.
    
    Returns:
    pd.DataFrame: A DataFrame with parsed and cleaned AQI data.
    """
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def analyze_aqi_trends(data):
    """
    Analyze AQI trends and correlate with major events.
    
    Parameters:
    data (pd.DataFrame): AQI data for different cities.
    """
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=data, x='Date', y='AQI', hue='City')
    plt.title('Air Quality Index Over Time for Major Cities')
    plt.xlabel('Date')
    plt.ylabel('AQI')
    plt.legend(title='City')
    plt.grid(True)

    # Highlight important dates or events
    important_dates = {
        '2023-01-01': 'New Year\'s Day',
        '2023-04-22': 'Earth Day',
        '2023-11-04': 'New emission laws enacted in several cities'
    }

    for date, event in important_dates.items():
        plt.axvline(x=date, color='red', linestyle='--', alpha=0.7)
        plt.text(date, plt.ylim()[1] * 0.95, event, rotation=90, color='red')

    plt.show()

# Example usage
file_path = 'data/aqi_data.csv'
aqi_data = load_and_prepare_data(file_path)
analyze_aqi_trends(aqi_data)