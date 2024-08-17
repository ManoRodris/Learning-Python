def binary_search(array, search):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left)//2
        if array[mid] == search:
            return mid
        elif array[mid] < search:
            left = mid + 1
        elif array[mid] > search:
            right = mid - 1
    return None

array = [3, 4, 5, 7, 9, 14, 24, 48]
search = int(input("Insert the number you want to search in the array: "))

index = binary_search(array, search)

if index is not None:
    print(f"The number can be found in the index {index} of the array")
else: 
    print("Number not found in the array")

