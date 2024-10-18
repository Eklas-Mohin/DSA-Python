def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break

def main():
    arr = [17, 23, 7, 59, 73, 13, 37, 53, 47]
    
    print('Unsorted Array:', arr, '\n')
    
    bubble_sort(arr)
    
    print('Sorted Array:  ', arr)

if __name__ == '__main__':
    main()
