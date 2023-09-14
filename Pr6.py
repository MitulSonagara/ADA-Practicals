import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate  # Import tabulate library
import sys
sys.setrecursionlimit(100000)

# Normal Quick Sort
def quick_sort(arr):
    global steps
    def partition(arr, low, high):
        steps = 0
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            steps += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1, steps

    def quick_sort_helper(arr, low, high):
        steps = 0
        if low < high:
            pi, steps = partition(arr, low, high)
            steps += quick_sort_helper(arr, low, pi - 1)
            steps += quick_sort_helper(arr, pi + 1, high)
        return steps

    n = len(arr)
    steps = 0
    start_time = time.time()
    steps = quick_sort_helper(arr, 0, n - 1)
    end_time = time.time()
    execution_time = (end_time - start_time)*1000
    return steps, execution_time

# Randomized Quick Sort
def randomized_quick_sort(arr):
    global steps
    def partition(arr, low, high):
        steps = 0
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            steps += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1, steps

    def quick_sort_helper(arr, low, high):
        steps = 0
        if low < high:
            pi, steps = partition(arr, low, high)
            steps += quick_sort_helper(arr, low, pi - 1)
            steps += quick_sort_helper(arr, pi + 1, high)
        return steps

    n = len(arr)
    steps = 0
    start_time = time.time()
    steps = quick_sort_helper(arr, 0, n - 1)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return steps, execution_time

# Function to generate a table of results
def generate_results_table(N):
    table_data = []
    for name, sort_func in sorting_algorithms:
        random_results = sort_func(generate_random_data(N))
        ascending_results = sort_func(generate_ascending_data(N))
        descending_results = sort_func(generate_descending_data(N))
        table_row = [name]
        for results in [random_results, ascending_results, descending_results]:
            steps, execution_time = results
            table_row.extend([f"{execution_time:.6f} ms", steps])
        table_data.append(table_row)
    headers = ["Algorithm", "Random Data (Time)", "Random Data (Steps)", "Ascending Data (Time)", "Ascending Data (Steps)", "Descending Data (Time)", "Descending Data (Steps)"]
    return tabulate(table_data, headers, tablefmt="pretty")

# Function to generate random data of size n
def generate_random_data(n):
    return [random.randint(1, 10000) for _ in range(n)]

# Function to generate ascending order data of size n
def generate_ascending_data(n):
    return list(range(1, n + 1))

# Function to generate descending order data of size n
def generate_descending_data(n):
    return list(range(n, 0, -1))

# Input 'N' from the user
try:
    N = int(input("Enter no. of elements 'N' that is to be sorted: "))
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
    sys.exit(1)

input_sizes = list(range(1, N + 251, 250))
sorting_algorithms = [
    ("Randomized quick sort", randomized_quick_sort),
    ("Quick Sort", quick_sort)
]

results = {"Random": {}, "Ascending": {}, "Descending": {}}

for size in input_sizes:
    for name, sort_func in sorting_algorithms:
        random_results = sort_func(generate_random_data(size))
        ascending_results = sort_func(generate_ascending_data(size))
        descending_results = sort_func(generate_descending_data(size))
        results["Random"].setdefault(name, []).append(random_results)
        results["Ascending"].setdefault(name, []).append(ascending_results)
        results["Descending"].setdefault(name, []).append(descending_results)


# Print the results
results_table = generate_results_table(N)
print(results_table)

# Plotting the results with thinner lines for time taken vs. no of inputs and steps vs. no of inputs
for data_type in results.keys():
    plt.figure(figsize=(12, 6))
    
    # Plotting time taken vs. no of inputs
    plt.subplot(1, 2, 1)
    for name in sorting_algorithms:
        times = [result[1] for result in results[data_type][name[0]]]
        plt.plot(input_sizes, times, label=name[0], linewidth=0.8)
    plt.xlabel("Number of Inputs")
    plt.ylabel("Time Taken (milliseconds)")
    plt.title(f"Time Taken vs. Number of Inputs ({data_type} Data)")
    plt.legend()
    plt.grid(True)

    # Plotting steps vs. no of inputs with a separate scale
    plt.subplot(1, 2, 2)
    for name in sorting_algorithms:
        steps = [result[0] for result in results[data_type][name[0]]]
        plt.plot(input_sizes, steps, label=name[0], linewidth=0.8)
    plt.xlabel("Number of Inputs")
    plt.ylabel("Steps Executed")
    plt.title(f"Steps vs. Number of Inputs ({data_type} Data)")
    plt.legend()
    plt.grid(True)
    plt.ticklabel_format(style='plain', axis='y')

    plt.tight_layout()
    plt.show()