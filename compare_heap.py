import time #to measure the time
import sys
import random #for random variable 

# Heapify function for Heapsort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Heapsort function
def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Quick Sort implementation
def quick_sort(arr): #Function for quick sort array
    if len(arr) <= 1: 
        return arr
    pivot = arr[len(arr) // 2] #Choosing pivot by median
    left = [x for x in arr if x < pivot] # Sending the element to the left if it is less then pivot
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] # Sending it to the right for greater than pivot
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(arr): #This is sorting function where the array is dividing into two parts
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) #Selecting till middle
    right = merge_sort(arr[mid:]) # after middle to the end
    return merge(left, right) #calling merge function

def merge(left, right): #merge function
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]) #adding the element the the left in sorting order
            i += 1
        else:
            result.append(right[j]) #adding it to the right
            j += 1
    result.extend(left[i:]) #adding the remaing element from left to the end
    result.extend(right[j:]) #adding remaining element from right to the end
    return result

# Function to test and measure performance
def test_sorting_algorithms(unsorted_array):
    random_array = [random.randint(1, 10) for _ in range(10)] #random 10 elements
    
    #setting the dataset
    datasets = {
        "Given Unsorted Array": unsorted_array,
        "Random Array": random_array
    }

    for name, dataset in datasets.items():
        print(f"{name}: {dataset}")
        
        # Quick Sort
        start_time = time.time() 
        quick_sorted = quick_sort(dataset)
        execution_time_qs = time.time() - start_time #measuring time
        memory_usage_qs = sys.getsizeof(quick_sorted) #size function to measure the memory usage 

        # Merge Sort
        start_time = time.time()
        merge_sorted = merge_sort(dataset)
        execution_time_ms = time.time() - start_time #measuring time
        memory_usage_ms = sys.getsizeof(merge_sorted) #size function to measure the size 
        
        # Heap Sort
        arr_copy = dataset.copy()
        start_time = time.time()
        heapsort(arr_copy)
        execution_time_hs = time.time() - start_time #measuring time
        memory_usage_hs = sys.getsizeof(arr_copy) #size function to measure the size
        

        # Output the results
        print(f"  Quick Sort - Sorted Array: {quick_sorted}")
        print(f"  Quick Sort - Time: {execution_time_qs:.6f} seconds, Memory: {memory_usage_qs} bytes")
        
        print(f"  Merge Sort - Sorted Array: {merge_sorted}")
        print(f"  Merge Sort - Time: {execution_time_ms:.6f} seconds, Memory: {memory_usage_ms} bytes")
        
        print(f"  Heap Sort - Sorted Array: {arr_copy}")
        print(f"  Heap Sort - Time: {execution_time_hs:.6f} seconds, Memory: {memory_usage_hs} bytes\n")
        
        # # Print reverse order
        # print(f"  Quick Sort - Reverse Order: {quick_sorted[::-1]}")
        # print(f"  Merge Sort - Reverse Order: {merge_sorted[::-1]}\n")
        
        # Measure time and memory for reverse order
        start_time = time.time()
        quick_sorted_reverse = quick_sorted[::-1] #sorting reversly
        execution_time_qs_rev = time.time() - start_time
        memory_usage_qs_rev = sys.getsizeof(quick_sorted_reverse)

        start_time = time.time()
        merge_sorted_reverse = merge_sorted[::-1] #sorting reversly
        execution_time_ms_rev = time.time() - start_time
        memory_usage_ms_rev = sys.getsizeof(merge_sorted_reverse)
        
        start_time = time.time()
        heap_sorted_reverse = arr_copy[::-1] #sorting reversly
        execution_time_hs_rev = time.time() - start_time
        memory_usage_hs_rev = sys.getsizeof(heap_sorted_reverse)

        print(f"  Quick Sort - Reverse Sorted Array: {quick_sorted_reverse}")
        print(f"  Quick Sort (Reverse) - Time: {execution_time_qs_rev:.6f} seconds, Memory: {memory_usage_qs_rev} bytes")
        
        print(f"  Merge Sort - Reverse Sorted Array: {merge_sorted_reverse}")
        print(f"  Merge Sort (Reverse) - Time: {execution_time_ms_rev:.6f} seconds, Memory: {memory_usage_ms_rev} bytes")
        
        print(f"  Heap Sort - Reverse Sorted Array: {heap_sorted_reverse}")
        print(f"  Heap Sort (Reverse) - Time: {execution_time_hs_rev:.6f} seconds, Memory: {memory_usage_hs_rev} bytes\n")


# Example unsorted array
unsorted_array = [10, 7, 8, 9, 1, 5, 15] 
#unsorted_array = [3, 4, 5, 6, 7, 9, 8, 10]

# Run the tests
test_sorting_algorithms(unsorted_array) # calling the function to test and measure
