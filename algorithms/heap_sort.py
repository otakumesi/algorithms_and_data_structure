def heap_sort(array) :
    for i in reversed(range(0, len(array)//2)):
        pushdown(array, i, len(array)-1)
    for j in reversed(range(1, len(array))):
        array[0], array[j] = array[j], array[0]
        pushdown(array, 0, j-1)
    return array


def pushdown(array, first, last):
    i = first
    while i <= (last-1)/2:
        if array[(2*i)+2] >= array[(2*i)+1] or (2*i)+2 >= last:
            j = (2*i)+1
        else:
            j = (2*i)+2
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
            i = j
        else:
            return

print(heap_sort([12, 23, 24, 45, 18, 11, 34]))
