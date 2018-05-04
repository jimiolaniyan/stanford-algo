def merge(left, right):
    arr = []
    nL = len(left)
    nR = len(right)
    i = 0
    j = 0

    while i < nL and j < nR:
        if left[i] <= right[j]:
            arr.append(left[i])
            i = i + 1
        else:
            arr.append(right[j])
            j = j + 1

    while i < nL:
        arr.append(left[i])
        i = i + 1

    while j < nR:
        arr.append(right[j])
        j = j + 1

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[: mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

