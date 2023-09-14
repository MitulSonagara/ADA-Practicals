#final1
import matplotlib.pyplot as plt
import numpy as np
import timeit
import sys
sys.setrecursionlimit(100000)

# Function 1: Calculate the sum using a loop
def calculate_sum_with_loop(N):
    start_time = timeit.default_timer()
    steps = 0  # Initialize step counter
    if N < 0:
        return "Please provide a non-negative integer for 'N'", steps
    sum = 0
    for i in range(1, N + 1):
        sum += i
        steps += 1  # Incrementing sum
    execution_time = (timeit.default_timer() - start_time)*1000
    return sum, steps, execution_time

# Function 2: Calculate the sum using a formula
def calculate_sum_with_formula(N):
    start_time = timeit.default_timer()
    steps = 0  # Initialize step counter
    if N < 0:
        return "Please provide a non-negative integer for 'N'", steps
    sum = N * (N + 1) // 2
    steps += 3  # Multiplication, addition, and integer division
    execution_time = (timeit.default_timer() - start_time)*1000
    return sum, steps, execution_time

# Function 3: Calculate the sum using tail recursion
def sum_recursive_tail(n, current_sum=0, current_step=0):
    start_time = timeit.default_timer()
    if n == 0:
        execution_time = (timeit.default_timer() - start_time)*1000
        return current_sum, current_step, execution_time
    result, steps, execution_time = sum_recursive_tail(n - 1, current_sum + n, current_step + 1)
    execution_time = (timeit.default_timer() - start_time)*1000
    return result, steps, execution_time

# Input 'N' from the user
try:
    N = int(input("Enter a non-negative integer for 'N': "))
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
    sys.exit(1)

# Calculate the sum using a loop
sum_loop, steps_loop, execution_time_loop = calculate_sum_with_loop(N)

# Calculate the sum using a formula
sum_formula, steps_formula, execution_time_formula = calculate_sum_with_formula(N)

# Calculate the sum using tail recursion
sum_recursive_result, steps_recursive, execution_time_recursive = sum_recursive_tail(N)

# Print the results
print(f"Number of steps executed in the loop function: {steps_loop}")
print(f"Execution time of the loop function: {execution_time_loop:.6f} ms")
print(f"Sum calculated by the loop function: {sum_loop}\n")

print(f"Number of steps executed in the formula function: {steps_formula}")
print(f"Execution time of the formula function: {execution_time_formula:.6f} ms")
print(f"Sum calculated by the formula function: {sum_formula}\n")

print(f"Number of steps executed in the recursive function: {steps_recursive}")
print(f"Execution time of the recursive function: {execution_time_recursive:.6f} ms")
print(f"Sum calculated by the recursive function: {sum_recursive_result}\n")

# Create a range of 'N' values for the graph
N_values = np.arange(1, N + 1)

# Initialize lists to store execution times for each method
execution_times_loop = []
execution_times_formula = []
execution_times_recursive = []
# Initialize lists to store step count for each method
steps_count_loop = []
steps_count_formula = []
steps_count_recursive = []

# Measure execution times for each 'N' value
for N in N_values:
    # Calculate the sum using a loop
    _, _, execution_time_loop = calculate_sum_with_loop(N)
    execution_times_loop.append(execution_time_loop)

    # Calculate the sum using a formula
    _, _, execution_time_formula = calculate_sum_with_formula(N)
    execution_times_formula.append(execution_time_formula)

    # Calculate the sum using tail recursion
    _, _, execution_time_recursive = sum_recursive_tail(N)
    execution_times_recursive.append(execution_time_recursive)


# Measure step count for each 'N' value
for N in N_values:
    # Calculate the sum using a loop
    _, steps_loop, _ = calculate_sum_with_loop(N)
    steps_count_loop.append(steps_loop)

    # Calculate the sum using a formula
    _, steps_formula, _ = calculate_sum_with_formula(N)
    steps_count_formula.append(steps_formula)

    # Calculate the sum using tail recursion
    _, steps_recursive, _ = sum_recursive_tail(N)
    steps_count_recursive.append(steps_recursive)
    
# Create a plot to visualize the data (execution time vs. N)
plt.figure(figsize=(10, 6))
plt.subplot(1,2,1)
plt.plot(N_values, execution_times_loop, label='Loop Method', marker='o', markersize=1)
plt.plot(N_values, execution_times_formula, label='Formula Method', marker='o', markersize=1)
plt.plot(N_values, execution_times_recursive, label='Recursive Method', marker='o', markersize=1)
plt.xlabel('N (Number of Integers to Sum)')
plt.ylabel('Execution Time (Milliseconds)')
plt.legend()
plt.title('Execution Time vs. N')

# Create a plot to visualize the data (execution time vs. N)
plt.subplot(1,2,2)
plt.plot(N_values, steps_count_loop, label='Loop Method', marker='o', markersize=1)
plt.plot(N_values, steps_count_formula, label='Formula Method', marker='o', markersize=1)
plt.plot(N_values, steps_count_recursive, label='Recursive Method', marker='o', markersize=1)
plt.xlabel('N (Number of Integers to Sum)')
plt.ylabel('Execution Steps')
plt.legend()
plt.title('Execution Steps vs. N')

# Show the plot
plt.tight_layout()
plt.show()