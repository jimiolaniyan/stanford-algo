def merge_count_split(left, right, counter):
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
            counter += len(left[i:])

    while i < nL:
        arr.append(left[i])
        i = i + 1

    while j < nR:
        arr.append(right[j])
        j = j + 1

    return counter, arr


def sort_count(arr):
    if len(arr) <= 1:
        return 0, arr

    mid = len(arr) // 2

    x, left = sort_count(arr[: mid])
    y, right = sort_count(arr[mid:])
    z, item = merge_count_split(left, right, x + y)
    return z, item


lines = [int(line) for line in open('/Users/jimiolaniyan/Documents/Dev/Courses/Design and Analysis of '
                                    'Algorithms/Week 1/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt')]


print(sort_count(lines))
