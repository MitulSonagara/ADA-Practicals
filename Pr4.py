import random
import timeit
import matplotlib.pyplot as plt

def linear_search(arr, target):
    steps = 0
    for i, element in enumerate(arr):
        steps += 1
        if element == target:
            return steps
    return steps

def binary_search(arr, target):
    steps = 0
    start, end = 0, len(arr) - 1
    while start <= end:
        steps += 1
        mid = (start + end) // 2
        if arr[mid] == target:
            return steps
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return steps

def generate_data(n):
    best_case_data = list(range(n))
    avg_case_data = random.sample(range(n), n)
    avg_case_data.sort()  # Ensure it's sorted for the worst case
    worst_case_data = list(range(n + 1, 2 * n + 1))
    return best_case_data, avg_case_data, worst_case_data

def analyze_search_performance(input_size_start, input_size_end):
    input_sizes = list(range(input_size_start, input_size_end + 1))
    linear_search_steps_best = []
    binary_search_steps_best = []
    linear_search_steps_avg = []
    binary_search_steps_avg = []
    linear_search_steps_worst = []
    binary_search_steps_worst = []
    linear_search_times_best = []
    binary_search_times_best = []
    linear_search_times_avg = []
    binary_search_times_avg = []
    linear_search_times_worst = []
    binary_search_times_worst = []

    for n in input_sizes:
        best_case_data, avg_case_data, worst_case_data = generate_data(n)
        target = best_case_data[0]

        # Measure steps and time for linear search
        linear_search_steps_best.append(linear_search(best_case_data, target))
        linear_search_steps_avg.append(linear_search(avg_case_data, target))
        linear_search_steps_worst.append(linear_search(worst_case_data, n))
        linear_search_time_best = timeit.timeit(lambda: linear_search(best_case_data, target), number=1)
        linear_search_time_avg = timeit.timeit(lambda: linear_search(avg_case_data, target), number=1)
        linear_search_time_worst = timeit.timeit(lambda: linear_search(worst_case_data, n), number=1)
        linear_search_times_best.append(linear_search_time_best)
        linear_search_times_avg.append(linear_search_time_avg)
        linear_search_times_worst.append(linear_search_time_worst)

        # Measure steps and time for binary search
        binary_search_steps_best.append(binary_search(best_case_data, target))
        binary_search_steps_avg.append(binary_search(avg_case_data, target))
        binary_search_steps_worst.append(binary_search(worst_case_data, n))
        binary_search_time_best = timeit.timeit(lambda: binary_search(best_case_data, target), number=1)
        binary_search_time_avg = timeit.timeit(lambda: binary_search(avg_case_data, target), number=1)
        binary_search_time_worst = timeit.timeit(lambda: binary_search(worst_case_data, n), number=1)
        binary_search_times_best.append(binary_search_time_best)
        binary_search_times_avg.append(binary_search_time_avg)
        binary_search_times_worst.append(binary_search_time_worst)

    # Create the first graph for binary search with subplots
    plt.figure(figsize=(12, 6))

    # Subplot 1: Steps vs. Input Size for Binary Search (All Cases)
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, binary_search_steps_best, label='Best Case')
    plt.plot(input_sizes, binary_search_steps_avg, label='Average Case')
    plt.plot(input_sizes, binary_search_steps_worst, label='Worst Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Steps Executed')
    plt.legend()
    plt.title('Binary Search Steps vs. Input Size')

    # Subplot 2: Time vs. Input Size for Binary Search (All Cases)
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, binary_search_times_best, label='Best Case')
    plt.plot(input_sizes, binary_search_times_avg, label='Average Case')
    plt.plot(input_sizes, binary_search_times_worst, label='Worst Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Binary Search Time vs. Input Size')

    # Create the second graph for linear search with subplots
    plt.figure(figsize=(12, 6))

    # Subplot 1: Steps vs. Input Size for Linear Search (All Cases)
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, linear_search_steps_best, label='Best Case')
    plt.plot(input_sizes, linear_search_steps_avg, label='Average Case')
    plt.plot(input_sizes, linear_search_steps_worst, label='Worst Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Steps Executed')
    plt.legend()
    plt.title('Linear Search Steps vs. Input Size')

    # Subplot 2: Time vs. Input Size for Linear Search (All Cases)
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, linear_search_times_best, label='Best Case')
    plt.plot(input_sizes, linear_search_times_avg, label='Average Case')
    plt.plot(input_sizes, linear_search_times_worst, label='Worst Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Linear Search Time vs. Input Size')

    plt.tight_layout()
    plt.show()

try:
    input_size_start = int(input("Enter the start of the input size range (e.g., 100): "))
    input_size_end = int(input("Enter the end of the input size range (e.g., 500): "))
    analyze_search_performance(input_size_start, input_size_end)
except ValueError:
    print("Invalid input. Please enter valid input sizes.")