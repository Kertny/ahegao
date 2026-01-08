import array

def shakersort(arr):
    min = 0
    max = len(arr) - 1
    for tes in range(len(arr)):
        for item in range(max):
            if arr[item] > arr[item + 1]:
                temp = arr[item]
                arr[item] = arr[item + 1]
                arr[item + 1] = temp
    return arr

test = False
print(not test)


A = [3, 9, 5, 7, 6, 4, 2, 1, 8]