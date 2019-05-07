def merge_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2;
    left = merge_sort(array[0:pivot])
    right = merge_sort(array[pivot:len(array)])
    return merge(left, right)

def merge(left, right):
    i, j, result = 0, 0, []
    while True:
        # i が left の長さを超えるまで繰り返す
        # また、j がすでに結果を追加し終わっているか、
        # right のほうが大きな値の場合に
        # right を result に追加する
        if i < len(left) and (j >= len(right) or left[i] < right[j]):
            result.append(left[i])
            i += 1
        # j が left の長さを超えるまで繰り返す
        # また、i がすでに結果を追加し終わっているか、
        # left のほうが大きな値の場合に
        # left を result に追加する
        if j < len(right) and (i >= len(left) or left[i] > right[j]):
            result.append(right[j])
            j += 1
        # 両方の追加が終わったらreturn
        if i == len(left) and j == len(right):
            return result

print(merge_sort([5, 2, 3, 1, 7]))
