def main():
    arr = [17, 23, 7, 59, 73, 13, 37, 53, 47]
    print('Unsorted Array:', arr, '\n')
    
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    print('Sorted Array:  ', arr)
    
if __name__ == "__main__":
    main()