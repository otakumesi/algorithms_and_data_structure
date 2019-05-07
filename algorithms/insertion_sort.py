def insertion_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

import pdb; pdb.set_trace()
