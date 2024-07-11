import numpy as np
import matplotlib.pyplot as plt

# Simulated temperature data from three sensors (in degrees Celsius)
sensor_data = {
    'Sensor1': np.random.normal(loc=22, scale=2, size=24),
    'Sensor2': np.random.normal(loc=23, scale=2, size=24),
    'Sensor3': np.random.normal(loc=21, scale=2, size=24)
}

def calculate_hourly_average(sensor_data):
    # Convert the dictionary of sensor data into a NumPy array for easier calculation
    data_array = np.array(list(sensor_data.values()))
    # Calculate the mean across rows (sensors) for each column (hour)
    hourly_averages = np.mean(data_array, axis=0)
    return hourly_averages

def plot_temperature(hourly_averages, threshold=25):
    hours = np.arange(1, 25)  # Array of hours from 1 to 24
    plt.figure(figsize=(10, 6))
    plt.plot(hours, hourly_averages, marker='o', linestyle='-', color='b')
    plt.axhline(y=threshold, color='r', linestyle='--')
    plt.title('Hourly Average Temperatures Over 24 Hours')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True)
    
    # Highlight hours where the average temperature exceeds the threshold
    above_threshold = hourly_averages > threshold
    plt.scatter(hours[above_threshold], hourly_averages[above_threshold], color='r')
    
    plt.show()

# Calculate the hourly averages
hourly_averages = calculate_hourly_average(sensor_data)
# Plot the results with a threshold of 25 degrees Celsius
plot_temperature(hourly_averages)