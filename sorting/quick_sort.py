from time import time

count = 0


def partition(arr, start, end):
    # select last element as pivot
    # arr[end - 1], arr[start] = arr[start], arr[end - 1]

    # select median as pivot
    if end - start > 2:
        ind = find_sub(arr, start, end)
        arr[ind], arr[start] = arr[start], arr[ind]

    pivot = arr[start]
    p_index = start + 1

    for i in range(p_index, end):
        if arr[i] < pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index = p_index + 1
    arr[start], arr[p_index - 1] = arr[p_index - 1], arr[start]
    return p_index - 1


def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index)
        quick_sort(arr, p_index + 1, end)
        return arr


def quick_sort_and_count(arr, start, end):
    global count
    if start < end:
        count += end - start - 1
        p_index = partition(arr, start, end)
        quick_sort_and_count(arr, start, p_index)
        quick_sort_and_count(arr, p_index + 1, end)
        return count, arr


def find_sub(arr, start, end):
    if (end - start) % 2 != 0:
        mid = (end - start) // 2
    else:
        mid = (end - start) // 2 - 1

    sub = [arr[start], arr[start + mid], arr[end - 1]]

    if (sub[1] < sub[0] <= sub[2]) or (sub[2] < sub[0] < sub[1]):
        return start
    elif (sub[0] < sub[1] < sub[2]) or (sub[2] < sub[1] < sub[0]):
        return start + mid
    else:
        return end - 1