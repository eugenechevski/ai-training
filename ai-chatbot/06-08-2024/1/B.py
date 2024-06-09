import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# Mock function to simulate real-time data fetching
def fetch_exchange_rates():
    now = datetime.now()
    rates = {
        'USD_EUR': np.random.uniform(0.8, 0.9),
        'USD_GBP': np.random.uniform(0.7, 0.8),
        'USD_JPY': np.random.uniform(100, 110)
    }
    return now, rates

def plot_live_data():
    plt.figure(figsize=(10, 6))
    plt.ion()  # Turn on interactive mode

    # Initialize lines and x-axis data
    times = []
    lines = []
    for _ in range(3):
        line, = plt.plot([], [])  # Initialize empty lines
        lines.append(line)

    plt.legend(lines, ['USD to EUR', 'USD to GBP', 'USD to JPY'])

    for _ in range(100):  # Simulate 100 new data points
        current_time, current_rates = fetch_exchange_rates()
        times.append(current_time)

        # Update lines with new data
        lines[0].set_xdata(times)
        lines[0].set_ydata([current_rates['USD_EUR']] * len(times))
        lines[1].set_xdata(times)
        lines[1].set_ydata([current_rates['USD_GBP']] * len(times))
        lines[2].set_xdata(times)
        lines[2].set_ydata([current_rates['USD_JPY']] * len(times))

        # Update x and y limits
        plt.xlim(min(times), max(times))
        plt.ylim(0.6, 1.1)  # Adjust y-axis limits based on your expected rate range

        plt.pause(0.1)  # Pause to update the plot

    plt.ioff()  # Turn off interactive mode
    plt.show()

plot_live_data()