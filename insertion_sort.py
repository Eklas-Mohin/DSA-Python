def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        idx = i - 1

        while idx >= 0 and arr[idx] > temp:
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = temp

def print_array(arr):
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    arr = [17, 23, 7, 59, 73, 13, 37, 53, 47]

    print("Unsorted Array:")
    print_array(arr)

    insertion_sort(arr)

    print("\nSorted Array:")
    print_array(arr)
