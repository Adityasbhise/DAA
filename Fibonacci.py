# Global variable to count steps in recursion
recursive_step_count = 0

def fibonacci_recursive(n):
    global recursive_step_count
    recursive_step_count += 1  # Increment the step count each time the function is called

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Global variable to count steps in iteration
iterative_step_count = 0

def fibonacci_iterative(n):
    global iterative_step_count
    iterative_step_count += 1  # Count the initial step for setting up base cases

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        iterative_step_count += 1  # Increment the step count for each iteration
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]
# Input the desired Fibonacci number 'n'
n = int(input("Enter the value of n: "))

# Reset step count for recursion and iteration
recursive_step_count = 0
iterative_step_count = 0

# Calculate Fibonacci using recursion and count steps
fib_recursive = fibonacci_recursive(n)
print(f"Fibonacci number (Recursive) for n = {n}: {fib_recursive}")
print(f"Number of steps (Recursive) to calculate Fibonacci number for n = {n}: {recursive_step_count}")

# Calculate Fibonacci using iteration and count steps
fib_iterative = fibonacci_iterative(n)
print(f"Fibonacci number (Iterative) for n = {n}: {fib_iterative}")
print(f"Number of steps (Iterative) to calculate Fibonacci number for n = {n}: {iterative_step_count}")

# Function to generate Fibonacci sequence up to n
def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    
    fibonacci_sequence = []
    a, b = 0, 1
    
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

# Generate and print the list of Fibonacci numbers up to 'n'
fib_sequence = generate_fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n}: {fib_sequence}")
