def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] > target:
            high = mid - 1  # Target is on the left side
        else:
            low = mid + 1  # Target is on the right side

    return -1  # Target not found

def main():
    arr = [1, 4, 6, 8, 9, 11, 14, 15, 20, 25, 33, 83, 87, 97, 99, 100]
    target = 20
    target_idx = binary_search(arr, target)

    if target_idx == -1:
        print("Target not found")
    else:
        print(f"Target is at index {target_idx}")

if __name__ == "__main__":
    main()

"""
    Binary Search is only applicable when the array is sorted
    Time Complexity is O(log2(n))
"""
