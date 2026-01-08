import array

def binary_search(arr, item):
    min = 0
    # len(arr) is -> indexerror: list index out of range
    # need subtract 1 to get the index of the last element
    max = len(arr) - 1
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            # Прибовляем, потому что элемент mid уже проверен
            min = mid + 1
        else:
            # Отнимаем, по принципу выше
            max = mid - 1
    return None

A = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

point = binary_search(A, 7)
