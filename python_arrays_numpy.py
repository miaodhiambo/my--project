import numpy as np

# 1. Using Lists (Built-in Python Arrays)
numbers = [10, 25, 34, 47, 52]

# Calculating sum, max, and min
total = sum(numbers)
largest = max(numbers)
smallest = min(numbers)

# Printing results
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Largest Number: {largest}")
print(f"Smallest Number: {smallest}\n")

# 2. Using NumPy Arrays
numbers_np = np.array([10, 25, 34, 47, 52])

# Performing calculations
mean_value = np.mean(numbers_np)
sum_value = np.sum(numbers_np)
std_dev = np.std(numbers_np)

# Printing results
print(f"NumPy Array: {numbers_np}")
print(f"Mean: {mean_value}")
print(f"Sum: {sum_value}")
print(f"Standard Deviation: {std_dev}")
