def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = search_pivot(array)
    left, right = [], []
    for val in array:
        if pivot > val:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + quick_sort(right)

def search_pivot(array):
    if array[0] > array[1]:
        return array[0]
    else:
        return array[1]

print(quick_sort([4, 6, 2, 1, 7]))
