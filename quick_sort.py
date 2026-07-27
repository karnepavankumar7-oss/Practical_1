import random
import time

def median_of_three(arr, low, high):
    """Median-of-three pivot selection to optimize performance."""
    mid = (low + high) // 2
    if arr[low] > arr[mid]: arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]: arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]: arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]

def hoare_partition(arr, low, high):
    """In-place Hoare partition scheme."""
    pivot = median_of_three(arr, low, high)
    left, right = low - 1, high + 1
    while True:
        while True:
            left += 1
            if arr[left] >= pivot: break
        while True:
            right -= 1
            if arr[right] <= pivot: break
        if left >= right: return right
        arr[left], arr[right] = arr[right], arr[left]

def quick_sort_recursive(arr, low, high):
    """Recursive Quick Sort driver."""
    if low < high:
        p_idx = hoare_partition(arr, low, high)
        quick_sort_recursive(arr, low, p_idx)
        quick_sort_recursive(arr, p_idx + 1, high)

def quick_sort(arr):
    """Main in-place Quick Sort API."""
    if not arr or len(arr) <= 1: return arr
    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    test_data = [29, 10, 14, 37, 13, -5, 0, 8, 24, 13]
    print(f"Original: {test_data}")
    quick_sort(test_data)
    print(f"Sorted:   {test_data}\n")

    data_size = 50_000
    large_data = [random.randint(-100000, 100000) for _ in range(data_size)]
    start = time.time()
    quick_sort(large_data)
    print(f"Sorted {data_size:,} items in {time.time() - start:.4f} seconds")
