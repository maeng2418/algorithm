def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    l = r = i = 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            a[i] = left[l]
            l += 1
            i += 1
        else:
            a[i] = right[r]
            r += 1
            i += 1

    while l < len(left):
        a[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        a[i] = right[r]
        r += 1
        i += 1

    return a

d = [2, 4, 5, 1, 3]

print(d)

print(merge_sort(d))
