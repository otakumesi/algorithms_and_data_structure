def selection_sort(array):
    for i in reversed(range(len(array))):
        max_idx = 0
        for j in range(1, i+1):
            if array[max_idx] < array[j]:
                max_idx = j
        array[i], array[max_idx] = array[max_idx], array[i]
    return array

print(selection_sort([3, 5, 1, 2, 7]))
import pdb; pdb.set_trace()
