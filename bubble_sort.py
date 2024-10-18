def bubble_sort(arr):
    n = len(arr)
    
    print('Unsorted Array:', arr, '\n')

    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    print('Sorted Array:  ', arr)

def main():
    arr = [17, 23, 7, 59, 73, 13, 37, 53, 47]
    bubble_sort(arr)

if __name__ == '__main__':
    main()
