def quick_sort(array, i, j):
    if i >= j:
        return []
    pivot = find_pivot(array, i, j)
    k = partition(array, i, j, pivot)
    quick_sort(array, i, k-1)
    quick_sort(array, k, j)

def find_pivot(array, i, j):
    for k in range(i, j+1):
        if array[i] != array[k]:
            if array[i] > array[k]:
                return array[i]
            else:
                return array[k]

def partition(array, l, r, pivot):
    while True:
        print(array, pivot, l, r, 'start')
        while array[l] < pivot:
            l += 1
        while array[r] >= pivot:
            r -= 1
        print(array, pivot, l, r, 'end')
        if l > r:
            return l
        array[l], array[r] = array[r], array[l]

array = [1, 5, 2, 4, 3]
quick_sort(array, 0, 4)
print(array)
