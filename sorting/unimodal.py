def unimodal(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    max_left = arr[mid-1]
    max_right = arr[mid]

    if max_right > max_left:
        return unimodal(arr[mid:])
    else:
        return unimodal(arr[:mid])


print(unimodal([2, 4, 7, 10, 13, 94, 66, 5, 4, 3, 1]))