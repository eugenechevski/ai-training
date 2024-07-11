import numpy as np
import matplotlib.pyplot as plt

# Simulated accuracies from 5 test runs of the model
accuracies = np.array([0.85, 0.88, 0.84, 0.67, 0.86])

def evaluate_model(accuracies):
    # Compute mean and standard deviation
    mean_accuracy = np.mean(accuracies)
    std_deviation = np.std(accuracies)

    print(f"Average Accuracy: {mean_accuracy:.2f}")
    print(f"Standard Deviation: {std_deviation:.2f}")

    # Compute median and interquartile range (IQR)
    median_accuracy = np.median(accuracies)
    iqr = np.subtract(*np.percentile(accuracies, [75, 25]))

    print(f"Median Accuracy: {median_accuracy:.2f}")
    print(f"Interquartile Range (IQR): {iqr:.2f}")

    # Detect outliers
    outliers = accuracies[np.abs(accuracies - mean_accuracy) > 2 * std_deviation]
    return outliers

outliers = evaluate_model(accuracies)
if outliers.size > 0:
    print("Outliers detected:", outliers)
else:
    print("No outliers detected.")

# Plot the accuracies
plt.figure(figsize=(8, 6))
plt.plot(accuracies, marker='o')
plt.title("Model Accuracies Over Multiple Runs")
plt.xlabel("Run Number")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()