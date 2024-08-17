def bubble_sort(array):
    limit = len(array) - 1
    for x in range(limit):
        exchange = True
        for y in range(limit):
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                exchange = False
        if exchange:
            break
    print(array)

array = [5, 9, 7, 24, 48, 3, 4, 14]

bubble_sort(array)