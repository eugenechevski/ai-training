import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib.animation import FuncAnimation

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
    fig, ax = plt.subplots(figsize=(10, 6))
    times, usd_eur_rates, usd_gbp_rates, usd_jpy_rates = [], [], [], []
    lines = [ax.plot([], [], label='USD to EUR')[0],
             ax.plot([], [], label='USD to GBP')[0],
             ax.plot([], [], label='USD to JPY')[0]]

    def init():
        ax.set_ylim(0, 1.1)  # Set initial y-axis limits
        ax.set_xlim(datetime.now(), datetime.now() + pd.Timedelta(seconds=10))  # Set initial x-axis limits
        ax.legend()
        return lines

    def update(frame):
        current_time, current_rates = fetch_exchange_rates()
        times.append(current_time)
        usd_eur_rates.append(current_rates['USD_EUR'])
        usd_gbp_rates.append(current_rates['USD_GBP'])
        usd_jpy_rates.append(current_rates['USD_JPY'])

        lines[0].set_data(times, usd_eur_rates)
        lines[1].set_data(times, usd_gbp_rates)
        lines[2].set_data(times, usd_jpy_rates)

        # Update x-axis limits to simulate a moving window
        ax.set_xlim(times[-1] - pd.Timedelta(seconds=10), times[-1])

        # Update y-axis limits to ensure all data points are visible
        ax.set_ylim(min(min(usd_eur_rates), min(usd_gbp_rates), min(usd_jpy_rates)) * 0.9,
                    max(max(usd_eur_rates), max(usd_gbp_rates), max(usd_jpy_rates)) * 1.1)

        return lines

    ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, interval=100)
    plt.show()

plot_live_data()