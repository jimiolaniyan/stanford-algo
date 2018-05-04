def rand_select(arr, k):
    if len(arr) < k:
        return None

    if len(arr) < 2:
        return arr[0]

    j = partition(arr)
    if j == k - 1:
        return arr[j]
    if j < k - 1:
        return rand_select(arr[j+1:], k - j - 1)
    if j > k - 1:
        return rand_select(arr[: j], k)


def partition(arr):
    pivot = arr[0]
    p_index = 1

    for i in range(p_index, len(arr)):
        if arr[i] < pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index = p_index + 1
    arr[0], arr[p_index - 1] = arr[p_index - 1], arr[0]
    return p_index - 1


print(rand_select([6, 5, 9, 7, 11, 10, 12, 8], 1))
