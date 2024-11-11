def heapify(arr, n, i):
    largest = i #initialize the largest
    left = 2 * i + 1 #left chid
    right = 2 * i + 2 #right child

    if left < n and arr[left] > arr[largest]: #If left is larger than the current largest
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr) #Getting the length of the array

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the largest element (root) with the last element
        heapify(arr, i, 0)

# Test the Heapsort implementation
arr = [10, 7, 8, 9, 1, 5, 15]
print("Original array:", arr)
heapsort(arr)
print("Sorted array:", arr)

