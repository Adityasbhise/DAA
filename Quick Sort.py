import random
import time

# Deterministic Partition Method
def deterministic_partition(arr, low, high):
    pivot = arr[low]  # Choose the first element as pivot
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Place pivot in the correct position
    return i - 1

# Randomized Partition Method
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Randomly choose a pivot index
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]  # Swap the pivot with the first element
    return deterministic_partition(arr, low, high)  # Use deterministic partitioning

# Deterministic Quick Sort Method
def deterministic_quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pivot_index = deterministic_partition(arr, low, high)
        
        # Print the array after partitioning
        print(f"Array after partitioning with pivot {arr[pivot_index]}: {arr}")
        
        # Recursively sort the left and right subarrays
        deterministic_quick_sort(arr, low, pivot_index - 1)
        deterministic_quick_sort(arr, pivot_index + 1, high)

# Randomized Quick Sort Method
def randomized_quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pivot_index = randomized_partition(arr, low, high)
        
        # Print the array after partitioning
        print(f"Array after partitioning with pivot {arr[pivot_index]}: {arr}")
        
        # Recursively sort the left and right subarrays
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

# Take user input for the array size and elements
n = int(input("Enter the size of the array: "))  # Get the size of the array
data = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))  # Get individual elements
    data.append(element)

# Analyze deterministic quick sort
print("\nDeterministic Quick Sort Steps:")
start_time = time.time()
deterministic_quick_sort(data.copy(), 0, len(data) - 1)
deterministic_time = time.time() - start_time
print("Deterministic Quick Sort Time:", deterministic_time)

# Analyze randomized quick sort
print("\nRandomized Quick Sort Steps:")
start_time = time.time()
randomized_quick_sort(data.copy(), 0, len(data) - 1)
randomized_time = time.time() - start_time
print("Randomized Quick Sort Time:", randomized_time)
