def quick_sort(a, start, end):
    if start >= end:
        return

    pivot = (start + end) // 2
    left, right = start, end

    while left <= right:
        while a[left] < a[pivot]:
            left += 1
        while a[right] > a[pivot]:
            right -= 1
        if left <= right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    # 왼쪽과 오른쪽이 서로 지나쳤으므로 다시 바꿔줌
    left, right = right, left

    quick_sort(a, start, left)
    quick_sort(a, right, end)
    return a

d = [2, 4, 5, 1, 3]
print(d)
print(quick_sort(d, 0, len(d)-1))