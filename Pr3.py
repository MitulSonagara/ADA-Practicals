#final

import random
import timeit
import matplotlib.pyplot as plt

def sequential_search(arr, target):
    steps = 0
    for element in arr:
        steps += 1
        if element == target:
            return steps
    return steps

def analyze_search_performance(input_sizes):
    best_case_steps = []
    avg_case_steps = []
    worst_case_steps = []
    best_case_times = []
    avg_case_times = []
    worst_case_times = []

    for n in input_sizes:
        best_case_data = list(range(n))
        avg_case_data = random.sample(range(n), n)
        worst_case_data = list(range(n + 1, 2 * n + 1))
        target = best_case_data[0]

        # Measure time for best case
        best_case_time = timeit.timeit(lambda: sequential_search(best_case_data, target), number=1)
        best_case_steps.append(sequential_search(best_case_data, target))
        best_case_times.append(best_case_time)

        # Measure time for average case
        avg_case_time = timeit.timeit(lambda: sequential_search(avg_case_data, target), number=1)
        avg_case_steps.append(sequential_search(avg_case_data, target))
        avg_case_times.append(avg_case_time)

        # Measure time for worst case
        worst_case_time = timeit.timeit(lambda: sequential_search(worst_case_data, n), number=1)
        worst_case_steps.append(sequential_search(worst_case_data, n))
        worst_case_times.append(worst_case_time)
    
    # Plotting steps vs n
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, best_case_steps, label='Best Case')
    plt.plot(input_sizes, avg_case_steps, label='Average Case')
    plt.plot(input_sizes, worst_case_steps, label='Worst Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Steps Executed')
    plt.legend()
    plt.title('Sequential Search Steps vs. Input Size')

    # Plotting time vs n
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, best_case_times, label='Best Case')
    plt.plot(input_sizes, avg_case_times, label='Average Case')
    plt.plot(input_sizes, worst_case_times, label='Worst Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Sequential Search Time vs. Input Size')

    plt.tight_layout()
    plt.show()

input_size_start = int(input("Enter the start of the input size range (e.g., 1000): "))
input_size_end = int(input("Enter the end of the input size range (e.g., 5000): "))
input_sizes = list(range(input_size_start, input_size_end + 251, 250))
analyze_search_performance(input_sizes)