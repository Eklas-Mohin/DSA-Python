def selection_sort(arr):
    n = len(arr)
    
    print('Unsorted Array:', arr, '\n')
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    
    print('Sorted Array:  ', arr)

def main():
    arr = [17, 23, 7, 59, 73, 13, 37, 53, 47]
    selection_sort(arr)

if __name__ == '__main__':
    main()
