def partition(arr, start, end):
    pivot = arr[start]
    p_index = start + 1

    for i in range(p_index, end):
        if arr[i] < pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index = p_index + 1
    arr[start], arr[p_index - 1] = arr[p_index - 1], arr[start]
    return p_index - 1


def _rselect(arr, start, end, k):
    if start < end:
        # return arr[start]
        j = partition(arr, start, end)
        if j == k - 1:
            return arr[j]
        if j > k - 1:
            return _rselect(arr, start, j, k)
        if j < k - 1:
            return _rselect(arr, j+1, end, k)


def rselect(arr, k):
    return _rselect(arr, 0, len(arr), k)


print(rselect([81, 15, 19, 72, 11, 0, 12, 17, 67, 4, 99, 42, ], 5))
