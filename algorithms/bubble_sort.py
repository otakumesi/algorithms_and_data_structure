def bubble_sort(array):
    for i in range(len(array)-2):
        for j in reversed(range(i+1, len(array)-1)):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

print(bubble_sort([4, 6, 1, 3, 7]))
