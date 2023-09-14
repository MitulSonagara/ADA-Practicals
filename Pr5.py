import timeit
import matplotlib.pyplot as plt

# Iterative method to find the nth Fibonacci number
def fibonacci_iterative(n):
    if n <= 1:
        return n, 1
    fib_prev = 0
    fib_curr = 1
    steps = 0
    for _ in range(2, n + 1):
        steps += 1
        fib_next = fib_prev + fib_curr
        fib_prev, fib_curr = fib_curr, fib_next
    return fib_curr, steps

# Recursive method to find the nth Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:
        return n, 1
    else:
        fib1, steps1 = fibonacci_recursive(n - 1)
        fib2, steps2 = fibonacci_recursive(n - 2)
        steps = steps1 + steps2 + 1
        return fib1 + fib2, steps

# Function to analyze the performance of both methods
def analyze_fibonacci_performance(n_values):
    iterative_steps = []
    recursive_steps = []
    iterative_times = []
    recursive_times = []

    for n in n_values:
        # Measure the steps and time for the iterative method
        start_time = timeit.default_timer()
        fib_value_iterative, steps_iterative = fibonacci_iterative(n)
        end_time = timeit.default_timer()
        iterative_steps.append(steps_iterative)
        iterative_times.append(end_time - start_time)

        # Measure the steps and time for the recursive method
        start_time = timeit.default_timer()
        fib_value_recursive, steps_recursive = fibonacci_recursive(n)
        end_time = timeit.default_timer()
        recursive_steps.append(steps_recursive)
        recursive_times.append(end_time - start_time)

    # Print the nth Fibonacci number and steps (both iterative and recursive)
    print(f"The {n}th Fibonacci number (Iterative): {fib_value_iterative}")
    print(f"Steps (Iterative): {steps_iterative}")
    print(f"The {n}th Fibonacci number (Recursive): {fib_value_recursive}")
    print(f"Steps (Recursive): {steps_recursive}")
    print()

    # Plotting steps vs input type and time vs input type
    plt.figure(figsize=(12, 6))

    # Subplot 1: Steps vs Input Type
    plt.subplot(1, 2, 1)
    plt.plot(n_values, iterative_steps, label='Iterative')
    plt.plot(n_values, recursive_steps, label='Recursive')
    plt.xlabel('Input Type (n)')
    plt.ylabel('Steps Executed')
    plt.legend()
    plt.title('Steps Executed vs Input Type')
    plt.ticklabel_format(style='plain', axis='y')

    # Subplot 2: Time vs Input Type
    plt.subplot(1, 2, 2)
    plt.plot(n_values, iterative_times, label='Iterative')
    plt.plot(n_values, recursive_times, label='Recursive')
    plt.xlabel('Input Type (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Time Taken vs Input Type')
    plt.ticklabel_format(style='plain', axis='y')


    plt.tight_layout()
    plt.show()


try:
    n = int(input("Enter the value of n to find the nth Fibonacci number: "))
    n_values = list(range(1, n + 1))
    analyze_fibonacci_performance(n_values)
except ValueError:
    print("Invalid input. Please enter a valid integer value for n.")